# -*- coding:utf-8 -*-
# time:2019/02/25 15:57

import json

lt = [
    {'sdg': '是德国'},
    {'sfgge': '的外观'},
]

string = json.dumps(lt)
ll = json.loads(string)
print(string)
print(ll)

json.dump(lt,open('json.txt','w',encoding="utf8"))
ht = json.load(open('json.txt', 'r', encoding="utf8"))
print(ht)