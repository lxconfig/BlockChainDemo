from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),  # 用户注册页面
    url(r'^register_handle$', views.register_handle, name='register_handle'),  # 用户注册处理页面
]
