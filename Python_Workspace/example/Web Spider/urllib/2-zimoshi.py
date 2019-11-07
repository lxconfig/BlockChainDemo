# -*- coding:utf-8 -*-
# time:2018/12/19 16:51

#正则表达式

# import re
# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
# ret = pattern.search(string)
# print(ret)

# import re
# string = '<div>如来佛祖</div></div></div>'
# pattern = re.compile(r'<div>.+?</div>')
# ret = pattern.search(string)
# print(ret)

# import re
# string = '''hate is a beautiful feel
# love you very much
# love she
# love her'''
# pattern = re.compile(r'^love', re.M)
# ret = pattern.findall(string)
# print(ret)

# import re
# string = '''<div>沁园春-雪
# 北国风光
# 千里冰封
# 万里雪飘
# 望长城内外
# 惟余莽莽
# 大河上下
# </div>'''
# pattern = re.compile(r'<div>(.*)</div>', re.S) #单行匹配（·可以匹配换行符）
# ret = pattern.findall(string)
# print(ret)

import re
string = 'i love you,you love me,ye'
pattern = re.compile(r'love')
ret = pattern.sub(r'love', 'hate', string)
print(ret)

# import re
# def fn(a):
#     ret = int(a.group())
#     print(ret)
#     return str(ret - 10)
# string = '身高175的女孩'
# pattern = re.compile(r'\d+')
# ret = pattern.sub(fn, string)
# print(ret)