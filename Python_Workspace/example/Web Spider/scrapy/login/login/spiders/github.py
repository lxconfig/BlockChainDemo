# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        utf8 = response.xpath('//input[@name="utf8"]/@value').extract_first()
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        webauthn_support = response.xpath('//input[@name="webauthn-support"]/@value').extract_first()
        post_data = {
            "utf8": utf8,
            "authenticity_token": authenticity_token,
            "webauthn-support": webauthn_support,
            "login": "lxconfig",
            "password": "shisan19960706"
        }
        yield scrapy.FormRequest(
            "http://github.com/session",
            formdata=post_data,
            callback=self.after_login,
        )
    def after_login(self, response):
        print(re.findall("lxconfig", response.text))

