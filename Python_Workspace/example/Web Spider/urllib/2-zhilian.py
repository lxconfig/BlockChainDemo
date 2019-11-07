# -*- coding:utf-8 -*-
# time:2019/01/06 16:26

# -*- coding:utf-8 -*-
# time:2019/01/09 14:41

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import time

class ZhiLianSpider:
    # 初始化变量
    def __init__(self, jl, kw, start_page, end_page):
        # 将上面的参数都保存为自己的成员属性
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.url = 'https://search.51job.com/list/030200,000000,0100,01,9,99,python,2,1.html?'
        # 创建一个空列表，存放所有工作信息
        self.items = []

    # 根据page拼接指定的url，然后生成请求对象
    def handle_request(self, page):
        url_now = self.url
        data = {
            'lang': 'c',
            'stype': '' ,
            'postchannel': '0000',
            'workyear': '99',
            'cotype': '99',
            'degreefrom': '99',
            'jobterm': '99',
            'companysize': '99',
            'providesalary': '99',
            'lonlat': '0,0',
            'radius': '-1',
            'ord_field': '0',
            'confirmdate': '9',
            'fromType': '',
            'dibiaoid': '0',
            'address': '',
            'line': '',
            'specialarea': '00',
            'from': '',
            'welfare': '',
        }
        handle_url = urllib.parse.urlencode(data)
        url_now = 'https://search.51job.com/list/030200,000000,0100,01,9,99,%s,2,%s.html?' % (self.kw, page)
        get_url = url_now + handle_url
        # 构建请求对象，发送请求
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        request = urllib.request.Request(get_url, headers= headers)
        return request

    # 解析内容
    def parse_content(self, content):
        # 生成对象
        soup = BeautifulSoup(content, 'lxml')
        # 先找到所有包含职位信息的div（一个岗位就是一个div）
        # 遍历这个div的列表，然后用div对象的select、find方法去找每一条记录的具体信息
        div_list = soup.find_all('div', class_ = 'el')[16:]   # 切片剔除不需要的数据
        # print(div_list)
        # print(len(div_list))

        # 遍历div_list,依次获取每一个数据
        for div in div_list:
            # select方法返回的始终是一个列表，所以要加下标[0]
            # 获取职位名称
            job_name = div.select('.t1 > span > a')[0]['title']
            # 获取公司名称
            firm_name = div.select('.t2 > a')[0]['title']
            # 获取工作地点
            job_address = div.select('.t3')[0].text
            # 获取薪资
            salary = div.select('.t4')[0].text
            # 获取职位发布时间
            post_time = div.select('.t5')[0].text

            # 将数据放到字典中
            item = {
                '职位名称': job_name,
                '公司名称': firm_name,
                '工作地点': job_address,
                '薪资福利': salary,
                '发布时间': post_time,
            }
            # 再存放到列表中
            self.items.append(item)

    # 开始爬取数据
    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            print('开始爬取第%s页' % page)
            request = self.handle_request(page)
            # 发送请求，获取内容
            content = urllib.request.urlopen(request).read().decode('gbk')
            # with open('1111.html', 'w', encoding='gbk') as f:
            #     f.write(content)
            # 解析内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)
            # 将列表数据保存到文件中
            string = json.dumps(self.items, ensure_ascii = False)
            with open('51job.txt', 'w', encoding='utf-8') as f:
                # 列表转换成字符串写入,或者用json格式写入
                f.write(string)
                # f.write(str(self.items))

def main():
    jl = input('请输入工作地点：')
    kw = input('请输入工作关键字：')
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    # 创建对象，启动爬取程序
    spider = ZhiLianSpider(jl, kw, start_page, end_page)
    spider.run()

if __name__ == '__main__':
    main()
