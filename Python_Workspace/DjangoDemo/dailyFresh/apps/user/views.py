from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse  # 反向解析
from apps.user.models import User
import re

# Create your views here.

# /user/register
def register(request):
    """用户注册页面"""
    return render(request, 'register.html')


# /user/register_handle
def register_handle(request):
    """用户注册处理"""
    # 获取页面传过来的值
    username = request.POST.get("user_name")
    password = request.POST.get("pwd")
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

    # 返回响应，跳转到首页
    return redirect(reverse("goods:index"))