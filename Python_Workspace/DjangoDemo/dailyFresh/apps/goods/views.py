from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from apps.goods.models import GoodsType,GoodsSKU,Goods,IndexGoodsBanner,IndexPromotionBanner,IndexTypeGoodsBanner
from django_redis import get_redis_connection
from django.core.cache import cache   # 设置django缓存
from apps.order.models import OrderGoods

# Create your views here.

# /goods
class IndexView(View):
    def get(self, request):
        """首页类视图"""
        # 首先查看缓存中是否存在数据
        context = cache.get('index_page_data')
        if context is None:
            """无缓存，则需要读取数据"""
            print("设置缓存")
            # 获取商品的种类信息
            types = GoodsType.objects.all()

            # 获取首页轮播商品的信息
            # 按index进行升序排列
            goods_banners = IndexGoodsBanner.objects.all().order_by('index')

            # 获取首页促销商品的信息
            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

            # 获取首页分类展示的商品信息(有图片及文字两种)
            # type_goods_banners = IndexTypeGoodsBanner.objects.all()
            for type in types:
                # 根据type种类，获取首页分类商品的文字信息和图片信息
                banners_title = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')
                banners_image = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
            
                # 动态的添加两种属性
                type.banners_title = banners_title
                type.banners_image = banners_image

            context = {
                "types": types,
                "goods_banners": goods_banners,
                "promotion_banners": promotion_banners,
            }
            # 设置缓存(key, value, timeout)
            cache.set('index_page_data', context, 3600)

        # 获取首页用户购物车商品数量
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            """判断用户是否登录"""
            # 链接redis数据库
            conn = get_redis_connection('default')
            cart_key = "cart_%s" % user.id
            # 获取hash的数目，既购物车商品的数量
            cart_count = conn.hlen(cart_key)

        # 组织上下文
        context.update(cart_count=cart_count)

        # 返回响应
        return render(request, 'index.html', context)


class DetailView(View):
    """商品详情类视图"""
    def get(self, request, goods_id):
        # 获取用户购物车信息
        user = request.user
        cart_count = 0
        if user.is_authenticated():
            conn = get_redis_connection("default")
            cart_key = "cart_%d" % user.id
            cart_count = conn.hlen(cart_key)
            
            # 添加用户的历史浏览记录
            histoty_key = "history_%d" % user.id
            # 移除redis中保存的相同的goods_id（不存在不会报错， 0表示全部移除）
            conn.lrem(histoty_key, 0, goods_id)
            # 添加用户的浏览商品id（向左侧添加）
            conn.lpush(histoty_key, goods_id)
            # 只保存用户的5条浏览记录(其余全部删除)
            conn.ltrim(histoty_key, 0, 4)
        
        # 获取商品分类信息
        types = GoodsType.objects.all()

        # 获取商品的详细信息
        try:
            goods_info = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            # 商品不存在
            return redirect(reverse("goods:index"))
        
        # 获取新品推荐信息,按创建时间降序排列
        new_goods_info = GoodsSKU.objects.filter(type=goods_info.type).order_by("-create_time")[:2]

        # 获取商品详情信息
        goods_detail = Goods.objects.get(name=goods_info.name)

        # 获取商品评论信息
        goods_comment = OrderGoods.objects.filter(sku=goods_info).exclude(comment="")

        # 组织上下文
        context = {
            "types": types,
            "goods_info": goods_info,
            "new_goods_info": new_goods_info,
            "goods_detail": goods_detail,
            "goods_comment": goods_comment,
        }

        # 返回响应
        return render(request, "detail.html", context)
