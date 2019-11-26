'''
@Author: lixuan
@Date: 2019-11-25 20:02:34
@LastEditTime: 2019-11-26 19:19:48
@Description: design modelClass
'''
from django.db import models

# Create your models here.
# 定义模型类

class BookInfo(models.Model):
    """图书模型类"""
    # CharField表示字段是字符串，长度为20
    book_title = models.CharField(max_length=20)
    # DateField表示字段是日期类型
    book_pub_date = models.DateField()

class HeroInfo(models.Model):
    """人物类"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    comment =  models.CharField(max_length=128)
    # 如果一个类(表)和其他类(表)存在一对多的关系，则需要在"多"中添加外键
    # hbook代表一个关系属性,在表中是：关系属性名_id
    hbook = models.ForeignKey("BookInfo")