from django.contrib import admin
from infotest.models import TestInfo
# Register your models here.

class TestInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "Info_title", "Info_price"]


# 注册应用
admin.site.register(TestInfo, TestInfoAdmin)