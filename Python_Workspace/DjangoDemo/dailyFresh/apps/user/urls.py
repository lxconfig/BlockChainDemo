from django.conf.urls import url
from apps.user.views import RegisterView, ActiveView, LoginView, verified_code

urlpatterns = [
    # url(r'^register$', views.register, name='register'),  # 用户注册页面
    # url(r'^register_handle$', views.register_handle, name='register_handle'),  # 用户注册处理页面
    url(r'^register$', RegisterView.as_view(), name="register"),  # 用户注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name="active"),  # 用户激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 用户登录
    # url(r'^verified_code$', verified_code, name='verified_code'),  # 用户登录
]
