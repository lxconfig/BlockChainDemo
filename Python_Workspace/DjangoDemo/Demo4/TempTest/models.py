from django.db import models
from tinymce.models import HTMLField  # 富文本编辑器

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

class PicTest(models.Model):
    '''上传图片模型类'''
    goods_pic = models.ImageField(upload_to='TempTest')  # upload_to表示图片上传到media文件夹下的哪个目录


class test(models.Model):
    """富文本编辑器实例"""
    STATUS_CHOICES = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.SmallIntegerField(default=1, choices = STATUS_CHOICES, verbose_name='状态')
    details = HTMLField(blank=True, verbose_name='详情')

    class Meta:
        db_table = 'tests'
        verbose_name = '富文本测试'
        verbose_name_plural = verbose_name
    
    # def __str__(self):
    #     return self.details
    