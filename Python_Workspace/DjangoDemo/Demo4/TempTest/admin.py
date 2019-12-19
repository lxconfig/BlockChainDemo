from django.contrib import admin
from TempTest.models import AreaInfo, PicTest, test

# Register your models here.

class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    # 额外的编辑条目数
    extra = 2

class AreaTabularInline(admin.TabularInline):
    # 写多类的名字
    model = AreaInfo
    # 额外的编辑条目数
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'area_name', 'parent_name', 'title']
    list_per_page = 10
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['area_name']  # 在页面右边增加过滤栏
    search_fields = ['area_name']  # 搜索框
    # fields = ['parent_name', 'area_name']  # 编辑页字段展示顺序
    # 将字段分组显示
    fieldsets = (
        ('基本', {'fields': ['area_name']}),
        ('高级', {'fields': ['parent_name']})
    )
    # 以块的形式展示关联数据
    # inlines = [AreaStackedInline]

    # 以表格的形式展示关联数据
    inlines = [AreaTabularInline]

admin.site.register(AreaInfo, AreaInfoAdmin)

admin.site.register(PicTest)

admin.site.register(test)