from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

from django_redis import get_redis_connection
from django.template import loader, RequestContext

# 如果任务处理者worker在其他电脑环境运行，则要在worker一端加入以下代码进行初始化
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyFresh.settings")
django.setup()
from apps.goods.models import GoodsType,IndexGoodsBanner,IndexPromotionBanner,IndexTypeGoodsBanner
# 创建一个Celery类的对象
# broker代表中间人，即任务存放的地方
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/2')


# 定义任务函数
# 即定义任务发起者
@app.task
def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    # 邮件主题（标题）
    subject = "天天生鲜-日夜兼程·急速送达"
    # 邮件正文,只能输入字符串
    message = ""
    # html_message可以解析html标签
    html_message = '<h1>%s, 欢迎您注册天天生鲜，请点击下面的链接激活账号!</h1><br/><a href="http://127.0.0.1:8000/user/active/%s"> \
    http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
    # 发件人
    sender = settings.EMAIL_FROM
    # 收件人
    receiver = [to_email]
    send_mail(subject, message, sender, receiver, html_message=html_message)


@app.task
def generate_static_index_html():
    """生成静态首页"""
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
    types.banners_title = banners_title
    types.banners_image = banners_image

    # 组织上下文
    context = {
        "types": types,
        "goods_banners": goods_banners,
        "promotion_banners": promotion_banners,
    }
    
    # 1. 加载模板文件，返回模板对象
    temp = loader.get_template("static_index.html")
    # 2. 模板渲染（返回标准的HTML文件）
    static_index_html = temp.render(context)  # 用传递的数据去替换HTML中的变量，得到标准HTML页面
    # 3. 生成首页对应的静态文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index_html)