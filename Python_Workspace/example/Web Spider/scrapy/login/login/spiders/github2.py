# -*- coding: utf-8 -*-
import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 自动从response中找到form表单，存在多个表单可以添加参数指定
            formdata={ # 键是对应的name值，值是要输入的值
                "login": "lxconfig",
                "password": "shisan19960706",
            },
            callback= self.after_login,
        )
    def after_login(self, response):
        print(re.findall("lxconfig", response.text))
