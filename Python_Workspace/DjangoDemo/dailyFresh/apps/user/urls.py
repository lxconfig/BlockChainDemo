from django.conf.urls import url
from apps.user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, UserAddressView
urlpatterns = [
    # url(r'^register$', views.register, name='register'),  # 用户注册页面
    # url(r'^register_handle$', views.register_handle, name='register_handle'),  # 用户注册处理页面
    url(r'^register$', RegisterView.as_view(), name="register"),  # 用户注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name="active"),  # 用户激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 用户登录
    url(r'^$', UserInfoView.as_view(), name='user_info'),  # 用户中心-信息页
    url(r'^order$', UserOrderView.as_view(), name='user_order'),  # 用户中心-订单页
    url(r'^address$', UserAddressView.as_view(), name='user_address'),  # 用户中心-地址页
]
