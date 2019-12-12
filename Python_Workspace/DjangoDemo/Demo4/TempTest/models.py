from django.db import models


# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField()
    class Meta:
        db_table = 'booktest_bookinfo'

class AreaInfo(models.Model):
    area_name = models.CharField(verbose_name = '地区', max_length=30)
    parent_name = models.ForeignKey('self', null=True, blank=True)
    
    def __str__(self):
        return self.area_name

    def title(self):
        return self.area_name
    title.admin_order_field = 'area_name'  # 自定义按什么字段进行排序(页面上可以点击)
    title.short_description = '地区名称'    # 自定义字段名

    class Meta:
        db_table = 'booktest_areainfo'