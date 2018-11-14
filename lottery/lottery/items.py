# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

print("定义爬取字段")
class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no = scrapy.Field()
    pre1 = scrapy.Field()
    pre2 = scrapy.Field()
    pre3 = scrapy.Field()
    pre4 = scrapy.Field()
    pre5 = scrapy.Field()
    heil1 = scrapy.Field()
    heil2 = scrapy.Field()
    data = scrapy.Field()
