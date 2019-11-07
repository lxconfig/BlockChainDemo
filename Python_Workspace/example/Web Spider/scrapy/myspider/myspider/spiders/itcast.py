# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名
    allowed_domains = ['itcast.cn'] # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最开始请求的url

    # 必须写成parse
    def parse(self, response):
        # 处理start_urls地址对应的响应
        # ret1 = response.xpath('//div[@class="tea_con"]//h3/text()').extract() # 提取内容
        # print(ret1)

        # 分组
        # li_list = response.xpath('//div[@class="tea_con"]//li')
        # for li in li_list:
        #     item = {}
        #     item["name"] = li.xpath('.//h30/text()').extract_first()
        #     item["title"] = li.xpath('.//h4/text()').extract_first()
        #     # print(item)
        #     # 必须返回Dict,Request,BaseItem,None,不能是list
        #     yield item
        for i in range(10):
            item = {}
            item["come_from"] = "itcast"
            # 通过warning等级把item输出
            logger.warning(item)
            yield item
