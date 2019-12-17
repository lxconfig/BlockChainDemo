from django.conf.urls import url
from TempTest import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^temp_var$', views.temp_var),
    url(r'^temp_tags$', views.temp_tags),
    url(r'^temp_filter$', views.temp_filter),
    url(r'^temp_inherit$', views.temp_inherit),
    url(r'^htmlzy$', views.html),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^change_pwd$', views.change_pwd),
    url(r'^change_pwd_action$', views.change_pwd_action),
    url(r'^verify_code$', views.verify_code),
    url(r'^url_reverse$', views.url_reverse),
    url(r'^show_args/(\d+)$', views.show_args, name='args'),
    url(r'^show_kwargs/(?P<a>\d+)/(?P<b>\d+)$', views.show_kwargs, name='kwargs'),
    url(r'^reverse_in_redirect$', views.reverse_in_redirect),
    url(r'^show_ip$', views.show_ip),
    url(r'^upload_pic$', views.upload_pic),
    url(r'^pic_handle$', views.pic_handle),
    url(r'^show_areas/(?P<index>\d*)$', views.show_areas),
    url(r'^sanji$', views.sanji),
    url(r'^prov$', views.prov),
    url(r'^city/(\d+)$', views.city),
    url(r'^country/(\d+)$', views.country),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_sessio),
]

