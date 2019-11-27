from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
# 定义视图函数

def Info(request):
    return render(
        request,
        "infotest/info.html",
        {
            "content": "test info!!",
            "list": list(range(1, 10)),
        }
    )