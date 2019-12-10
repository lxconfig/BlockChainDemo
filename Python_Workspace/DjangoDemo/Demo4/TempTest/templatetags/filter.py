# 自定义过滤器

from django.template import Library

# 创建一个Library类的对象
register = Library()

# 至少有一个参数，但最多两个
@register.filter
def mod(num):
    return num % 2 == 0

@register.filter
def mod_val(num, value):
    return num % value == 0