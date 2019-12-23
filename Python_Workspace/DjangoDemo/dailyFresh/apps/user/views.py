from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse  # 反向解析
from apps.user.models import User
import re
from django.views.generic import View         # 类视图需要继承的类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  # 加密用户的身份信息
from itsdangerous import SignatureExpired  # 加密数据过期的异常
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

# /user/register
# def register(request):
#     if request.method == "GET":
#         # GET请求
#     else:
#         # post请求

class RegisterView(View):
    """用户注册类视图"""
    def get(self, request):
        # get请求对应的处理
        """用户注册页面"""
        return render(request, 'register.html')
    
    def post(self, request):
        # post请求对应的处理
        """用户注册处理"""
        # 获取页面传过来的值
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        c_password = request.POST.get("cpwd")
        email = request.POST.get("email")
        agreement = request.POST.get("allow")
        
        # 进行数据校验
        # 判断用户是否都输入了相关数据
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {"errorMsg": "数据输入不完整"})
        
        # 判断邮箱格式是否合法
        pattern = r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
        if not re.match(pattern, email):
            # 邮箱格式不正确
            return render(request, 'register.html', {'errorMsg': '邮箱格式错误'})
        
        # 判断密码长度是否在8-20位
        if len(password) not in range(8, 21):
            return render(request, 'register.html', {'errorMsg': '密码长度应在8-20位'})

        # 判断两次密码是否一致
        if password != c_password:
            return render(request, 'register.html', {'errorMsg': '两次输入的密码不一致'})
        
        # 判断是否同意了注册协议
        if agreement != 'on':
            return render(request, 'register.html', {'errorMsg': '请同意注册协议'})
        
        # 判断用户名是否存在于数据库中
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None
        if user:
            return render(request, 'register.html', {"errorMsg": "用户名已存在"})    
        
        # 进行业务处理： 注册用户
        # 直接调用create_user创建新用户
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        # 注册后，应该给用户发一封邮件，地址是:http://127.0.0.1/user/active/1
        # 1代表用户的id，是用户的唯一标识，但是直接发送1不安全，需要加密这个唯一标识
        info = {'confirm': user.id}
        serializer  = Serializer(settings.SECRET_KEY, 3600)
        token = serializer.dumps(info)
        # 去掉解密出来的字符串前面的b字符
        token = token.decode()

        # 发邮件
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
        receiver = [email]
        send_mail(subject, message, sender, receiver, html_message=html_message)
        # 返回响应，跳转到首页
        return redirect(reverse("goods:index"))


class ActiveView(View):
    """用户激活类视图"""
    def get(self, request, token):
        """进行用户激活"""
        serializer = Serializer(settings.SECRET_KEY, 3600)
        # 解密拿到信息
        try:
            info = serializer.loads(token)
            user_id = info['confirm']
            # 根据user_id在数据库中查找对应用户，修改is_active字段
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            # 跳转登录页面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            # 真正的项目应该会再点击发送激活链接
            return HttpResponse('激活链接已过期')


class LoginView(View):
    """用户登录类视图"""
    def get(self, request):
        return render(request, 'login.html')




