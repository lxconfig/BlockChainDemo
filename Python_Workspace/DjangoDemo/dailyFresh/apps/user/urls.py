from django.conf.urls import url
from apps.user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, UserAddressView
from django.contrib.auth.decorators import login_required  #  django认证系统自带的登录装饰器
urlpatterns = [
    # url(r'^register$', views.register, name='register'),  # 用户注册页面
    # url(r'^register_handle$', views.register_handle, name='register_handle'),  # 用户注册处理页面
    url(r'^register$', RegisterView.as_view(), name="register"),  # 用户注册
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name="active"),  # 用户激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 用户登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 用户注销登录
    # url(r'^$', login_required(UserInfoView.as_view()), name='user_info'),  # 用户中心-信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='user_order'),  # 用户中心-订单页
    # url(r'^address$', login_required(UserAddressView.as_view()), name='user_address'),  # 用户中心-地址页
    # 定义mixin类，则不用每个视图都写上login_required()
    url(r'^$', UserInfoView.as_view(), name='user_info'),  # 用户中心-信息页
    url(r'^order$', UserOrderView.as_view(), name='user_order'),  # 用户中心-订单页
    url(r'^address$', UserAddressView.as_view(), name='user_address'),  # 用户中心-地址页
]
