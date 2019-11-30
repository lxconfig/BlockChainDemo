from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(\d+)$', views.delete),  # 捕获url的参数(位置参数)
    url(r'area', views.area),
    url(r'^test/(?P<arg>\w+=\d+)',views.test),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check)
]