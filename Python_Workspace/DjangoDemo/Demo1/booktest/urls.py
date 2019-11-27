from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置项
    url(r'^index', views.index),  # 建立/index和index()之间的关系
    url(r'^books$', views.show_books),
    url(r'^books/(\d+)$', views.detail)  # 通过分组把参数传递给视图函数
]