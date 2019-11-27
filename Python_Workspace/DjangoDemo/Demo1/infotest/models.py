from django.db import models

# Create your models here.
# 创建模型类

class TestInfo(models.Model):
    Info_title = models.CharField(max_length=20)
    Info_price = models.CharField(max_length=10)