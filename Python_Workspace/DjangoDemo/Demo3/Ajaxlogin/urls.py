from django.conf.urls import url
from Ajaxlogin import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^common_login$', views.common_login),
    url(r'^common_login_check$', views.common_login_check),
    url(r'^login_check$', views.login_check),
    url(r'^index$', views.index),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
    url(r'^loginOut$', views.loginOut),
]