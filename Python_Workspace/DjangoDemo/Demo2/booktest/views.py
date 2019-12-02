from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from booktest.models import BookInfo, HeroInfo, AreaInfo, UserInfo

# Create your views here.

def index(request):
    books = BookInfo.objects.all()
    return render(
        request,
        'booktest/index.html',
        {
            "books": books,
        }
    )

def create(request):
    """新增一本图书信息"""
    book = BookInfo()
    book.btitle = "流星蝴蝶剑"
    book.bpub_date = "1985-03-13"
    book.bread = 100
    book.bcomment = 14
    book.save()
    # return index(request)
    # 新增完后让页面跳转回/index页面  重定向页面
    return HttpResponseRedirect(redirect_to='/index')



def delete(request, id):
    """删除一本图书信息"""
    book = BookInfo.objects.get(id=id)
    book.delete()
    # return HttpResponseRedirect(redirect_to="/index")
    return redirect(to="/index")


def area(request):
    # 广州市信息
    area = AreaInfo.objects.get(area_name="广州市")
    # 上级城市
    up_area = area.parent_name
    # 下级城市
    down_area = area.areainfo_set.all()
    return render(
        request,
        "booktest/area.html",
        {
            "area": area,
            "up_area": up_area,
            "down_area": down_area,
        }
    )

def test(request, arg):
    return HttpResponse(arg)


def login(request):
    return render(request, 'booktest/login.html')

def login_check(request):
    # request.POST  post提交的参数
    # request.GET   get提交的参数
    # 都是QueryDict的对象，类似字典
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == "lixuan" and password == "123":
        return HttpResponse('ok')
    else: 
        return HttpResponse('error')

def ajax_test(request):
    # 显示ajax页面
    return render(request, 'booktest/ajax_test.html')

def ajax_handle(request):
    # ajax请求处理
    return JsonResponse({"res": 1})  # 会被转换为JSON数据传给data