# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/889370168/profile']

    def start_requests(self):
        cookies = "anonymid=jtwizms2-e2tnjc; depovince=GUZ; jebecookies=ddc108ef-fac1-4c3d-b1bd-2f5f20b85a22|||||; _r01_=1; JSESSIONID=abcXsIDS32VGAgk5RxsNw; ick_login=91e8e3fb-3e73-4da2-ad63-7de3bd0c85e8; _de=B192BF27B05F9FB0E2A69D838E8B6F33696BF75400CE19CC; p=10a2b5ab86ae988a66871e514e00209f8; first_login_flag=1; ln_uact=525868229@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/women_main.gif; t=0328b79672612c7660a0ccfb98ca19e88; societyguester=0328b79672612c7660a0ccfb98ca19e88; id=889370168; xnsid=2da0b0ad; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies=cookies)
    def parse(self, response):
        print(re.findall("李龙", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/889370168/profile?v=info_timeline",
            callback=self.parse_detail,
        )
    def parse_detail(self, response):
        print(re.findall("李龙", response.body.decode()))
