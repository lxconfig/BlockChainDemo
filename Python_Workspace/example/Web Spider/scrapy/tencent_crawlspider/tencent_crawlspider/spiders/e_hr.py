# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

logger = logging.getLogger(__name__)

class EHrSpider(CrawlSpider):
    name = 'e_hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+\#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        tr_list = response.xpath('//table[@class="tablelist"]/tr')[1: -1]
        for tr in tr_list:
            item["title"] = tr.xpath('./td[1]/a/text()').extract_first()
            item["publish_time"] = tr.xpath('./td[5]/text()').extract_first()
            logger.warning(item)
        return item
