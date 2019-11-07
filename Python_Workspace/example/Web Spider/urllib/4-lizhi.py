# -*- coding:utf-8 -*-
# time:2018/12/25 14:16

import urllib.request
import urllib.parse
import re
import os

def handle_url(url, page):
    url = url + str(page) + '.html'
    return url

def download_content(res):
    def download_image(a):
        src = a.group()
        url = src.split('"')[1]
        image_url = "http://www.yikexun.cn" + url
        image = urllib.request.urlretrieve(image_url)
        return image_url
    pattern = re.compile(r'<div class="neirong">.*?<p>(.*?)</div>', re.S)
    ret = pattern.findall(res)
#    print(ret)
#    print(len(ret))
    text = ret[0]
    # 将内容里面的所有图片信息全部清空
    pat = re.compile(r'<img .*?>')
    text = pat.sub(download_image, text)
    return text

def get_title_url(response,page):
    pattern = re.compile(r'<div class="art-t">.*?<h3><a href="(.*?)">(.*?)</a></h3>', re.S)
    ret = pattern.findall(response)
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    dir_name = "励志语录"
    # secondary_name = "第%s页" % page
    # paths = dir_name + '\\' + secondary_name
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # if not os.path.exists(paths):
    #     os.mkdir(paths)
    for each in ret:
        title_url = "http://www.yikexun.cn" + each[0]
        title = each[-1]
        request = urllib.request.Request(title_url, headers=headers)
        res = urllib.request.urlopen(request).read().decode()
        # 每个标题对应的内容
        text = download_content(res)
        # print(text)
        # exit()
        # 将内容和标题拼接起来，写入文件中
        string = "<h1>%s</h1>%s" % (title, text)
        path = dir_name + '\\' + "励志.html"
        with open(path, 'a', encoding="utf-8") as f:
            f.write(string)

        # 分不同页写入文件中
        # file_name = each[0].split('/')[-1]
        # path = paths + '\\' + file_name
        # with open(path, 'w', encoding="utf-8") as f:
        #     print("%s内容正在下载" % file_name)
        #     f.write(res)
        #     print("%s内容下载完成" % file_name)

def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        # 拼接url
        print("第%s页开始读取..." % page)
        sentence_url = handle_url(url, page)
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        request = urllib.request.Request(sentence_url, headers=headers)
        response = urllib.request.urlopen(request).read().decode()
        get_title_url(response, page)
        print("第%s页读取成功..." % page)

if __name__ == '__main__':
    main()