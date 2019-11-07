# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    def parse(self, response):
        tr_list = response.xpath('//div[@class="greyframe"]/table[2]/tr/td/table/tr')
        # 分组
        for tr in tr_list:
            item = YangguangItem()
            item["ID"] = tr.xpath('./td[1]/text()').extract_first()
            item["title"] = tr.xpath('./td[2]/a[2]/@title').extract_first()
            item["href"] = tr.xpath('./td[2]/a[2]/@href').extract_first()
            item["status"] = tr.xpath('./td[3]/span/text()').extract_first()
            item["user_name"] = tr.xpath('./td[4]/text()').extract_first()
            item["publish_time"] = tr.xpath('./td[5]/text()').extract_first()
            print(item)
            # yield scrapy.Request(item["href"], callback=self.parse_detail, meta={"item": item})
        # 翻页
        # next_url = response.xpath('//div[@class="pagination"]/a[text()=">"]/@href').extract_first()
        # if next_url is not None:
        #     yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response): # 处理详情页
        item = response.meta["item"]
        item["content"] = response.xpath('//div[@class="wzy1"]/table[2]/tr[1]/td//text()').extract()
        item["content_img"] = response.xpath('//div[@class="wzy1"]/table[2]/tr/td/div/img/@src').extract()
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        yield item