# -*- coding:utf-8 -*-
# time:2018/12/19 14:37
import urllib.request
import urllib.parse

url = 'http://www.renren.com/969169522/profile'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie':
        'anonymid=jput3htlh8juua; depovince=GUZ; _r01_=1; '
        'ick_login=e0290d98-077c-4cc9-b5e6-5ad4093ca9ed; loginfrom=null; '
        'jebe_key=1148a331-e8aa-40d9-b4b7-4bcef88dc48d%7Cf7ec8a258207cdffc2c28e22c338172d%7C1545201576123%7C1%7C1545201574508; '
        'wpsid=15235267976057; wp_fold=0; t=3f2caf32c3c51a9742698c3094a69ea42; '
        'societyguester=3f2caf32c3c51a9742698c3094a69ea42; '
        'id=969169522; xnsid=3aca3bde; jebecookies=66033855-fc34-41c7-a8e6-5bdd80aedcc9|||||; ver=7.0',
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

with open('renren.html', 'wb') as f:
    f.write(response.read())