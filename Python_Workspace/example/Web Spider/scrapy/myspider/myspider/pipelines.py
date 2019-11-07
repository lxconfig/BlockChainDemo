# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

logger = logging.getLogger(__name__)

class MyspiderPipeline(object):
    # 必须写process_item
    def process_item(self, item, spider):
        if spider.name == "itcast":
            logger.warning("__" * 4)

# class MyspiderPipeline1(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item