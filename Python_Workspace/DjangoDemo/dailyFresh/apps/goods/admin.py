from django.contrib import admin
from apps.goods.models import Goods, GoodsImage, GoodsSKU, GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
from django.core.cache import cache
# Register your models here.


class BaseModel(admin.ModelAdmin):
    """商品种类模型管理器类"""
    def save_model(self, request, obj, form, change):
        """新增或更新表中的数据时调用"""
        super().save_model(request, obj, form, change)

        # 发出任务，让celery_worker重新生成静态首页
        # 导入模块不要写到函数外，否则启动不了项目
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')
    
    def delete_model(self, request, obj):
        """删除表中的数据时调用"""
        super().delete_model(request, obj)

        # 发出任务，让celery_worker重新生成静态首页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')


class GoodsAdmin(BaseModel):
    pass

class GoodsImageAdmin(BaseModel):
    pass

class GoodsTypeAdmin(BaseModel):
    pass

class GoodsSKUAdmin(BaseModel):
    pass

class IndexGoodsBannerAdmin(BaseModel):
    pass

class IndexPromotionBannerAdmin(BaseModel):
    pass

class IndexTypeGoodsBannerAdmin(BaseModel):
    pass

admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsImage, GoodsImageAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)