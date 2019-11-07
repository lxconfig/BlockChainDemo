# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/']

    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]/tr')[1: -1]
        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath('./td[1]/a/text()').extract_first()
            item["position"] = tr.xpath('./td[2]/text()').extract_first()
            item["publish_time"] = tr.xpath('./td[5]/text()').extract_first()
            # print(item)
            # yield item
        next_url = response.xpath('//a[@id="next"]/@href').extract_first()
        # print(next_url)
        if next_url != 'javascript:;':
            next_url = "https://hr.tencent.com/" + next_url
            # print(next_url)
            yield scrapy.Request(next_url, callback=self.parse1, meta={"item": item})

    def parse1(self, response):
        it = response.meta["item"]