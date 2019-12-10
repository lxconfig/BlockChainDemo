from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from TempTest.models import BookInfo

# Create your views here.

def index(request):
    temp = loader.get_template('TempTest/index.html')
    context = RequestContext(request, {})
    res_html = temp.render(context)
    return HttpResponse(res_html)

def temp_var(request):
    my_dict = {"title": '字典键值'}
    my_list = [1,2,4,6,3,5]
    book = BookInfo.objects.get(id=1)
    context = {
        'dict': my_dict,
        'list': my_list,
        'book': book,
    }
    return render(request, 'TempTest/temp_var.html', context)

def temp_tags(request):
    books = BookInfo.objects.all()
    return render(request, 'TempTest/temp_tags.html', {'books': books})

def temp_filter(request):
    books = BookInfo.objects.all()
    return render(request, 'TempTest/temp_filter.html', {'books': books})

def temp_inherit(request):
    return render(request, 'TempTest/child.html')

def html(request):
    return render(request, 'TempTest/htmlzy.html', {'content': '<h1>html转义</h1>'})

def login(request):
    # 先判断用户是否已经登录过
    if request.session.has_key('isLogin'):  # session是否包含某个key
        # 用户已登录
        return redirect('/change_pwd')
    else:
        # 用户未登录
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'TempTest/login.html', {'username': username})

def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')  # 点击后传过来的是on，否则是None
    if username == 'lixuan' and password == '123':
        response = redirect('/change_pwd')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
        # 只要session中包含isLogin字段，则表示用户已经登录
        request.session['isLogin'] = True
        return response
    else:
        return redirect('/login')


# 登录判断的装饰器函数
def login_required(function):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('isLogin'):
            return function(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrapper


@login_required
def change_pwd(request):
    return render(request, 'TempTest/change_pwd.html')

@login_required
def change_pwd_action(request):
    pwd = request.POST.get('pwd')
    return HttpResponse("修改密码为:%s" % pwd)