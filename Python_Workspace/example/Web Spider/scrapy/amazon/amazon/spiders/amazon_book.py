# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonBookSpider(RedisCrawlSpider):
    name = 'amazon_book'
    allowed_domains = ['amazon.cn']
    redis_key = "amazon"

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="left_nav browseBox"]/ul/li',)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@aria-live="polite"]/li/span',)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="a-row a-spacing-small"]/div/a',)), callback='parse_item'),
        # 翻页
        Rule(LinkExtractor(restrict_xpaths=('//span[@class="pagnRA"]',)), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item["book_title"] = response.xpath('//div[@class="a-section a-spacing-none"]/h1/span[1]/text()').extract()
        item["book_title"] = [i.strip() for i in item["book_title"]]
        item["book_author"] = response.xpath('//div[@id="bylineInfo"]/span/a/text()').extract()
        item["book_price"] = response.xpath('//a[@class="a-button-text"]/span[2]/span/text()').extract()
        item["book_price"] = [i.strip() for i in item["book_price"]]
        print(item)

