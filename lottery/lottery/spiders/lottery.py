import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from lottery.items import LotteryItem
from lottery.sql import Sql
print("爬取数据")
class Myspider(scrapy.Spider):
    name = "ticket"
    allowed_domains = ['lottery.gov.cn']
    base_url = "http://www.lottery.gov.cn/historykj/history_"
    end_url = ".jspx?_ltype=dlt"

    # 每一页
    def start_requests(self):
        for i in range(1,86):
            url = self.base_url + str(i) + self.end_url
            yield Request(url,self.parse)

    # 获取每一页的数据
    def parse(self,response):
        trs = BeautifulSoup(response.text, 'lxml').find('div',class_='result').find('table').find('tbody').findAll('tr')
        for tr in trs:
            # 前区
            pre = tr.findAll('td',class_='red')
            pre1 = pre[0].get_text()
            pre2 = pre[1].get_text()
            pre3 = pre[2].get_text()
            pre4 = pre[3].get_text()
            pre5 = pre[4].get_text()
            # 后区
            heil = tr.findAll('td',class_='blue')
            heil1 = heil[0].get_text()
            heil2 = heil[1].get_text()
            # 期号
            No = tr.find('td').get_text()
            # 日期
            data = tr.findAll('td')[-1].get_text()

            # item = LotteryItem()
            # item['no'] = No
            # item['pre1'] = pre1
            # item['pre2'] = pre2
            # item['pre3'] = pre3
            # item['pre4'] = pre4
            # item['pre5'] = pre5
            # item['heil1'] = heil1
            # item['heil2'] = heil2
            # item['data'] = data
            Sql.insert(No, pre1, pre2, pre3, pre4, pre5, heil1, heil2, data)
            # yield item