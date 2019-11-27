from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo

# Create your views here.
# 定义视图函数
def index(request):
    # return HttpResponse("xxxx")
    # return myrender(request, "booktest/index.html")

    # Django已经写好了这样的封装
    return render(
        request,
        "booktest/index.html",
        {
            "content": "hello Django",
            "list": list(range(1, 10))
        }
    )

# 上面这些过程可以封装在一个函数中
# def myrender(request, template_path, context_dict={}):
#     # 1. 加载模板文件，返回模板对象
#     temp = loader.get_template(template_path) # 不用写templates/booktest...
#     # 2. 定义模板上下文（向模板文件传递数据）
#     context = RequestContext(request, context_dict)  # 数据用字典传送
#     # 3. 模板渲染（返回标准的HTML文件）
#     res_html = temp.render(context)  # 用传递的数据去替换HTML中的变量，得到标准HTML页面
#     # 4. 返回给浏览器
#     return HttpResponse(res_html)


def show_books(request):
    books = BookInfo.objects.all()  # 通过M获取所有图书信息
    return render(
        request,
        "booktest/show_books.html",  # 通过T返回页面
        {
            "books": books,
        }
    )


def detail(request, id):
    book = BookInfo.objects.get(id=id)
    heros = book.heroinfo_set.all()
    return render(
        request,
        'booktest/detail.html',
        {
            "book": book,
            "heros": heros,
        }
    )