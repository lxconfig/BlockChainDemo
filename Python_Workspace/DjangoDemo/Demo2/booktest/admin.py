from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, UserInfo

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
admin.site.register(UserInfo)
