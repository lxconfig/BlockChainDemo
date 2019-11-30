from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    comment =  models.CharField(max_length=128)
    # 如果一个类(表)和其他类(表)存在一对多的关系，则需要在"多"中添加外键
    # hbook代表一个关系属性,在表中是：关系属性名_id
    hbook = models.ForeignKey("BookInfo")
    # 删除标记
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    """地级市自关联"""
    # 城市名
    area_name = models.CharField(max_length=30)
    # 关联属性（一对多类型）
    parent_name = models.ForeignKey('AreaInfo', null=True, blank=True)

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)