from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from TempTest.models import BookInfo, PicTest, AreaInfo
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
import random
from django.core.urlresolvers import reverse
from Demo4 import settings
from django.core.paginator import Paginator

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
    user_verified_code = request.POST.get('verified_code')   # 用户输入的验证码
    io_verified_code = request.session.get('verified_code')  # session保存的验证码
    if user_verified_code != io_verified_code:
        return redirect('/login')
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

def verify_code(request):
    # 定义变量，用于画面的背景色，宽，高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width, height = 100, 25
    # 创建画布对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的候选字符
    str1 = 'ABCD1234EFGHI567JKLMNOPQRST8UVWX90YZ'
    # 随机取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，进行验证
    request.session['verified_code'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，类型为png
    return HttpResponse(buf.getvalue(), 'image/png')

def url_reverse(request):
    return render(request, 'TempTest/url_reverse.html')

def show_args(request, a):
    return HttpResponse('a = %s' % a)

def show_kwargs(request, a, b):
    return HttpResponse('a = %s, b = %s' % (a, b))

def reverse_in_redirect(request):
    # url为动态生成的地址
    url = reverse('TempTest:index')
    # print(url)
    return redirect(url)

def show_ip(request):
    # 可以拒绝某些ip访问网站
    # exclude_ip = ['10.21.21.115']
    # user_ip = request.META['REMOTE_ADDR']
    # if user_ip in exclude_ip:
    #     return HttpResponse('<h1>Forbidden</h1>')
    return render(request, 'TempTest/show_ip.html', {'user_ip': user_ip})

def upload_pic(request):
    """用户上传图片"""
    return render(request, 'TempTest/upload_pic.html')

def pic_handle(request):
    """上传图片处理"""
    # 1. 获取上传文件的处理对象
    pic = request.FILES['pic']  # 'pic'是input项的name值
    # print(type(pic))
    # 2. 创建一个文件写入图片的数据
    save_path = '%s/TempTest/%s' % (settings.MEDIA_ROOT, pic.name)  # 图片保存的路径，pic.name表示上传文件的名字
    with open(save_path, 'wb') as f:
        # pic.chunks()返回一个生成器，每次返回图片文件的一小块
        for content in pic.chunks():
            f.write(content)
    # 3. 在数据库中保存上传记录
    PicTest.objects.create(goods_pic='TempTest/%s' % pic.name)
    # 4. 返回响应
    return HttpResponse('ok')

def show_areas(request, index):
    # 1. 查询数据库数据
    areas = AreaInfo.objects.filter(parent_name__isnull=True)
    # 2. 分页，每页显示10条, paginator是Paginator类的对象
    paginator = Paginator(areas, 10)
    # 3. 获取第一页的内容,pages是Page类的对象(可遍历)，其属性object_list是包含第一页内容的查询集
    if index == '':
        index = 1
    else:
        index = int(index)
    pages = paginator.page(index)
    print(pages.previous_page_number())
    # 4. 返回响应
    return render(request, 'TempTest/show_areas.html', {'pages': pages})