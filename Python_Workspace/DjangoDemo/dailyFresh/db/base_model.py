'''
@Author: lixuan
@Date: 2019-12-19 14:47:52
@LastEditTime : 2019-12-19 14:48:03
@Description: 定义模型类抽象基类
'''
from django.db import models

class BaseModel(models.Model):
    """模型类抽象基类"""
    # 所有模型类都继承此类
    # 为所有表添加下面三个字段
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象类
        abstract = True