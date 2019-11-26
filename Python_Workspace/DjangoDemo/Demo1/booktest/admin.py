from django.contrib import admin
from booktest.models import BookInfo, HeroInfo  # 导入模型类(应用名booktest不可少)


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ["id", "book_title", "book_pub_date"]

class HeroInfoAdmin(admin.ModelAdmin):
    """人物模型管理类"""
    list_display = ["id", "name", "gender", "comment", "hbook_id"]
# Register your models here.
# 注册应用 并自定义显示内容
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)