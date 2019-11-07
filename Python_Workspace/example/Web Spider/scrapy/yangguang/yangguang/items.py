# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    ID = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    status = scrapy.Field()
    user_name = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()