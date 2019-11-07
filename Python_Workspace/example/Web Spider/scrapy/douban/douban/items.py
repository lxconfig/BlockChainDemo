# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    arts = scrapy.Field()
    WenXue = scrapy.Field()
    popular = scrapy.Field()
    culture = scrapy.Field()
    life = scrapy.Field()
    econ = scrapy.Field()
    scinece = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    price = scrapy.Field()
    publish_time = scrapy.Field()
    summary = scrapy.Field()
    href = scrapy.Field()

