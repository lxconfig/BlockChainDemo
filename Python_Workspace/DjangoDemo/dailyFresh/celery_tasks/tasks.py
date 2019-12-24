from celery import Celery
from django.conf import settings
from django.core.mail import send_mail

# 如果任务处理者worker在其他电脑环境运行，则要在worker一端加入以下代码进行初始化
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyFresh.settings")
# django.setup()

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