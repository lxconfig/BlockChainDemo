from django.conf.urls import url
from infotest import views

urlpatterns = [
    url(r'^Info', views.Info),
]