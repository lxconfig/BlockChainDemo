# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ProverbSpider(scrapy.Spider):
    name = 'proverb'
    allowed_domains = ['proverb.cn']
    start_urls = ['https://www.gushiwen.org/']

    def parse(self, response):
        item = {}
        proverb_name = response.xpath('//div[@class="cont"]/p/a/b/text()').extract()
        proverb_cont = response.xpath('//div[@class="cont"]/div[@class="contson"]/text()').extract()
        item = {
            '诗名': proverb_name,
            '诗体': proverb_cont,
        }
        # print(item)
        # yield item
        logger.warning(item)

