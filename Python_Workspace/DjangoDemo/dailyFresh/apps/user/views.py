from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse  # 反向解析
from apps.user.models import User, Address
import re
from django.views.generic import View         # 类视图需要继承的类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer  # 加密用户的身份信息
from itsdangerous import SignatureExpired  # 加密数据过期的异常
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from celery_tasks.tasks import send_register_active_email  # 导入发送邮件任务函数
from django.contrib.auth import authenticate, login, logout        # 导入django自带登录验证及登录信息保存session模块,登出模块
from PIL import Image, ImageDraw, ImageFont                # 加入验证码
from django.utils.six import BytesIO
import random
from utils.mixin import LoginRequiredMixin                 # mixin类,需要登录后才能访问的页面先继承此类

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
        # 使用celery异步发送邮件
        # 使用delay方法将任务放到中间人里
        send_register_active_email.delay(email, username, token)

        # # 邮件主题（标题）
        # subject = "天天生鲜-日夜兼程·急速送达"
        # # 邮件正文,只能输入字符串
        # message = ""
        # # html_message可以解析html标签
        # html_message = '<h1>%s, 欢迎您注册天天生鲜，请点击下面的链接激活账号!</h1><br/><a href="http://127.0.0.1:8000/user/active/%s"> \
        # http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
        # # 发件人
        # sender = settings.EMAIL_FROM
        # # 收件人
        # receiver = [email]
        # send_mail(subject, message, sender, receiver, html_message=html_message)
        
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
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked}) 

    def post(self, request):
        """登录校验"""
        # 接收数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errorMsg': '数据不完整'})
        # 判断用户名与密码是否匹配
        user = authenticate(username=username, password=password)

        if user is not None:
            # 用户名与密码正确
            if user.is_active:
                # 用户已激活
                # 记录用户登录状态(保存信息到session中)
                login(request, user)
                # 获取登录之后，要跳转到的url,并且设置默认值(next值不一定总是存在)
                next_url = request.GET.get('next', reverse('goods:index'))
                # 跳转到next_url
                response = redirect(next_url)
                remember = request.POST.get('remember')
                if remember == 'on':
                    # 需要记住用户名
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    # 不需要记住用户名
                    response.delete_cookie('username')
                return response
            else:
                return render(request, 'login.html', {'errorMsg': '账户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errorMsg': '用户名或密码错误'})


# /user/logout
class LogoutView(View):
    """用户注销登录类视图"""
    def get(self, request):
        # 使用Django自带的登出功能
        # 清除session信息
        logout(request)
        return redirect(reverse('goods:index'))


# /user
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""
    def get(self, request):
        # 返回一个值判断哪个页面被选中了
        return render(request, 'user_center_info.html', {"page": 'user'})


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    """用户中心-订单页"""
    def get(self, request):
        # 用户页面顶端的欢迎信息：在用户登录后，应该显示用户名，而不再显示 登录 注册
        # Django为每个请求都提供了一个request.user属性，并传递给模板页面
        # 如果用户没有登录：request.user设置成AnonymousUser的一个实例
        # 如果用户登录：request.user设置成User的一个实例
        # 可以用request.user.is_authenticated()方法判断是否登录
        return render(request, 'user_center_order.html', {"page": 'order'})


# /user/address
class UserAddressView(LoginRequiredMixin, View):
    """用户中心-地址页"""
    def get(self, request):
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None

        # 通过自定义模型管理器类对象来查询是否有默认地址
        address = Address.objects.get_default_address(user)

        # 获取所有地址
        all_address = Address.objects.get_all_address(user)
        return render(request, 'user_center_site.html', {"page": 'address', 'address': address, 'all_address': all_address})
    
    def post(self, request):
        """用户增加收货地址"""
        # 获取数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 检验数据
        if not all([receiver, addr, phone]):
            # 数据不完整
            return render(request, 'user_center_site.html', {"errorMsg": '数据不完整!'})
        
        if not re.match(r'^1[3|4|5|7|8|9][0-9]{9}$', phone):
            # 电话号码有误
            return render(request, 'user_center_site.html', {"errorMsg": '电话号码有误!'})
        
        # 业务处理：添加地址
        # 能进入这个地址说明已经登录过，那么就会有request.user属性，并且是一个User实例
        user = request.user
        # 根据user及is_default判断当前用户是否存在默认地址
        # 如果不存在，则把此时用户输入的地址作为默认地址
        # 如果存在，则只存储此时用户输入的地址

        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None

        # 通过自定义模型管理器类对象来查询是否有默认地址
        address = Address.objects.get_default_address(user)
        
        if address:
            is_default = False
        else:
            is_default = True
        # 添加地址
        Address.objects.create(user=user, receiver=receiver, addr=addr, zip_code=zip_code, phone=phone, is_default=is_default)

        # 返回响应
        # get请求
        return redirect(reverse('user:user_address'))