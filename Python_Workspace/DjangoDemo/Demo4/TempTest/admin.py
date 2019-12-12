from django.contrib import admin
from TempTest.models import AreaInfo

# Register your models here.

class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'area_name', 'parent_name', 'title']
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['area_name']  # 在页面右边增加过滤栏
    search_fields = ['area_name']  # 搜索框

admin.site.register(AreaInfo, AreaInfoAdmin)