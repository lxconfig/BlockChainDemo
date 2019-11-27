from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from booktest.models import BookInfo, HeroInfo

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
