# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from copy import deepcopy

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/']

    def parse(self, response):
        item = DoubanItem()
        item["arts"] = response.xpath('//a[@name="文学"]/@name').extract_first()  # 文学
        arts_target = response.xpath('//div[@class=""]/div[1]//table[1]/tbody/tr//td')
        for art in arts_target:
            item["WenXue"] = "https://book.douban.com" + art.xpath('./a/@href').extract_first()
            yield scrapy.Request(item["WenXue"], callback=self.parse_detail, meta={"item": deepcopy(item)})

    def parse_detail(self, response):
        item = response.meta["item"]
        item["name"] = response.xpath('//div[@class="info"]/h2/a/@title').extract()
        item["href"] = response.xpath('//div[@class="info"]/h2/a/@href').extract_first()
        yield scrapy.Request(item["href"], callback=self.parse_book_detail, meta={"item": deepcopy(item)})

    def parse_book_detail(self, response):
        item = response.meta["item"]
        item["author"] = response.xpath('div[@id="info"]/a[1]/text()').extract_first()
        item["press"] = response.xpath('div[@id="info"]/span[2]/text()').extract_first()
        item["price"] = response.xpath('div[@id="info"]/span[8]/text()').extract_first()
        item["publish_time"] = response.xpath('div[@id="info"]/span[6]/text()').extract_first()
        print(item)



