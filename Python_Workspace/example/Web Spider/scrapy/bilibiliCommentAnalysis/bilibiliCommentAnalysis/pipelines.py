# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import jieba
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt

class BilibilicommentanalysisPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "comment":
            comment_text = open(r"message.txt", 'r',encoding="utf-8").read()
            cut_text = " ".join(jieba.cut(comment_text))
            color_mask = imread("back.jpg")
            cloud = WordCloud(
                scale=4,
                # width=500,
                # height=500,
                font_path="STSONG.TTF",
                background_color="white",
                max_words=3000,
                # min_font_size=30,
                max_font_size=60,
                mask=color_mask,
            )
            word_cloud = cloud.generate(cut_text)
            word_cloud.to_file("demo.jpg")
            plt.imshow(word_cloud)
            plt.axis('off')
            plt.show()
        return item
