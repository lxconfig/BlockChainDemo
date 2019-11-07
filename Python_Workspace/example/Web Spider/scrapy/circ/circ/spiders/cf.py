# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['bxjg.circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    # 自定义提取url地址的规则
    # 自动将url地址补充完整
    rules = (
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'), # 提取第一页数据的url地址
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True), # 提取下一页的url地址
    )

    def parse_item(self, response):
        item = {}
        item["title"] = re.findall('<!--TitleStart-->(.*?)<!--TitleEnd-->', response.body.decode())[0]
        item["publish_date"] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})", response.body.decode())[0]
        print(item)
