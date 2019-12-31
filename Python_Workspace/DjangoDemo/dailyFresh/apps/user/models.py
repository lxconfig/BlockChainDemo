'''
@Author: lixuan
@Date: 2019-12-19 15:06:15
@LastEditTime : 2019-12-31 14:30:04
@Description: 用户模型
'''
from django.db import models
from django.contrib.auth.models import AbstractUser  # 导入抽象用户类
from db.base_model import BaseModel  # 导入模型类抽象基类
from django.conf import settings
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# Create your models here.

# 一类
class User(AbstractUser, BaseModel):
    """用户模型类"""
    # def generate_active_token(self):
    #     """生成用户签名字符串"""
    #     serializer = Serializer(settings.SECRET_KEY, 3600)
    #     info = {'confirm': self.id}
    #     token = serializer.dumps(info)
    #     return token.decode()
    
    class Meta:
        db_table = 'df_user'
        # 在后台管理页面显示自定义表名
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    

class AddressManager(models.Manager):
    """地址模型管理器类"""
    def get_default_address(self, user):
        # 获取用户的默认收货地址
        try:
            address = self.get(user=user, is_default=True)
        except Address.DoesNotExist:
            address = None
        
        return address
    
    def get_all_address(self, user):
        # 获取用户所有的地址
        try:
            all_address = self.filter(user=user)
        except Address.DoesNotExist:
            all_address = None
        
        return all_address


# 多类
class Address(BaseModel):
    """用户地址模型类(收件地址)"""
    user = models.ForeignKey('User', verbose_name = '所属账户')  # 关联属性，对应于User表
    receiver = models.CharField(max_length=20, verbose_name = '收件人')
    addr = models.CharField(max_length=256, verbose_name = '收件地址')
    zip_code = models.CharField(max_length=6, verbose_name = '邮政编码')
    phone = models.CharField(max_length=11, verbose_name = '联系电话')
    is_default = models.BooleanField(default=False, verbose_name = '是否默认')

    # 创建一个地址模型管理器类的对象
    objects = AddressManager()

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name