# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy
import urllib.parse

class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://dangdang.com/']
    redis_key = "dangdang"

    def parse(self, response):
        div_list = response.xpath('//div[@class="con flq_body"]/div')
        # 大分类
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip()) > 0]
            dl_list = div.xpath('./div//dl[@class="inner_dl"]')
            # 二级分类
            for dl in dl_list:
                item["m_cate"] = dl.xpath('./dt//text()').extract()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip()) > 0][0]
                # 三级分类
                a_list = dl.xpath('./dd/a')
                for a in a_list:
                    item["s_href"] = a.xpath('./@href').extract_first()
                    if item["s_href"] :
                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.parse_book_detail,
                            meta = {"item": deepcopy(item)}
                        )
    def parse_book_detail(self, response):
        item = response.meta["item"]
        li_list = response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            item["book_img"] = li.xpath('./a/img/@src').extract_first()
            item["book_name"] = li.xpath('./p[1]/a/text()').extract_first()
            item["book_desc"] = li.xpath('./p[2]/text()').extract_first()
            item["book_price"] = li.xpath('./p[3]/span[@class="search_now_price"]/text()').extract_first()
            item["book_author"] = li.xpath('./p[@class="search_book_author"]//text()').extract()
            item["book_author"] = li.xpath('./p[@class="search_book_author"]/span[1]//text()').extract()
            item["book_publish_date"] = li.xpath('./p[@class="search_book_author"]/span[2]/text()').extract_first()
            item["book_press"] = li.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            print(item)
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_detail,
                meta={"item": item}
            )

