# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
print("保存爬取字段")
from .sql import Sql
from lottery.items import LotteryItem

class LotteryPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,LotteryItem):
            no = item['no']
            pre1 = item['pre1']
            pre2 = item['pre2']
            pre3 = item['pre3']
            pre4 = item['pre4']
            pre5 = item['pre5']
            heil1 = item['heil1']
            heil2 = item['heil2']
            data = item['data']
            Sql.insert(no,pre1,pre2,pre3,pre4,pre5,heil1,heil2,data)
            print("保存成功")
