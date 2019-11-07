# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import jsonpath


logger = logging.getLogger(__name__)
class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/web-interface/ranking/region?jsonp=jsonp&rid=95&day=7', # 视频json
                  'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={}&sort=0', ] # 评论json

    def start_requests(self):
        cookies = "buvid3=43DDB271-B133-46FA-AF01-1D98B957672A48988infoc; LIVE_BUVID=AUTO8515538329271215; sid=6000udoo; DedeUserID=577850; DedeUserID__ckMd5=628f716f2acb3618; SESSDATA=32a61077%2C1556424973%2C28322b31; bili_jct=a40961308d3734a1f50283150f8fecc1; stardustvideo=1; CURRENT_FNVAL=16; rpdid=iwkwxioiwidosskqpiwqw; CURRENT_QUALITY=80; bp_t_offset_577850=237022971435694537; _dfcaptcha=74ff95fb0603e0501f5842349d723c33"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies,
        )
    def parse(self, response):
        obj = json.loads(response.text)
        aid = jsonpath.jsonpath(obj, '$.data..aid')
        for id in aid:
            url = self.start_urls[1].format(id)
            yield scrapy.Request(
                url,
                callback= self.parse_comment,
            )
    def parse_comment(self, response):
        item = {}
        obj = json.loads(response.text)
        user_name = jsonpath.jsonpath(obj, '$.data.replies..member.uname')
        content = jsonpath.jsonpath(obj, '$.data.replies..content.message')
        with open("message.txt", 'a', encoding="utf-8") as f:
            f.write(str(content))
        message = dict(zip(user_name, content))
        item.update(message)
        logger.warning(item)
        yield item

