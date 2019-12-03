from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta

# Create your views here.

def login(request):
    return render(request, 'Ajaxlogin/login.html')

def common_login(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'Ajaxlogin/common_login.html', {'username': username})

def common_login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')  # 点击后传过来的是on，否则是None
    if username == 'lixuan' and password == '123':
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
        return response
    else:
        return redirect('/common_login')

def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # username = request.GET.get('username')
    # password = request.GET.get('password')

    if username == 'lixuan' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

def index(request):
    return render(request, 'Ajaxlogin/index.html')

def set_cookie(request):
    # 必须是HttpResponse类的对象，或其子类的对象才能设置cookie
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num，值为1
    response.set_cookie('num', 1)
    # 设置过期时间,max_age表示多少秒后过期
    # response.set_cookie('num', 1, max_age=14*24*3600)
    # expires表示多少天后过期
    # response.set_cookie('num', 1, expires=datetime.now()+timedelta(day=14))
    # 返回cookie给浏览器
    return response

def get_cookie(request):
    # 取cookie的值
    num = request.COOKIES['num']
    return HttpResponse(num)