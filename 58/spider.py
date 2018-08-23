# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/8/8 9:39
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import time

class Spilser:
    MYSQL_HOSTS = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_PORT = '3306'
    MYSQL_DB = 'spider'
    MYSQL_CHARACTERS = 'utf8'
    start_url = "http://jn.58.com/zufang/"
    end_url = "/?PGTID=0d300008-0010-949d-5b51-0c3c76da6d56&ClickID=2"
    count = 0
    headers = {
        'Connection': 'keep-alive',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    def getRoom(self):
        for i in range(1,70):
            request_url = self.start_url + 'pn' + str(i) + self.end_url
            print("访问的url: " + request_url)
            print("处理的页数："+str(i))
            count = 0
            response = requests.get(request_url, headers=self.headers).text
            rooms_infos = BeautifulSoup(response, 'lxml').find('ul', class_='listUl').findAll('li')
            print("休眠5秒，防止被封杀")
            time.sleep(5)
            for room_info in rooms_infos:
                try:
                    title = room_info.find('div', class_='des').find('h2').get_text().strip()
                    address = room_info.find('div', class_='des').find('p', class_='add').get_text().strip().replace(
                        " ", '').replace("\n", '')
                    room = room_info.find('div', class_='des').find('p', class_='room').get_text().strip()
                    room_num = room.split(" ")[0].strip()
                    room_area = room.split(" ")[-1].strip()
                    money = room_info.find('div', class_='money').get_text().strip()
                    count = count + 1
                    self.save_data(title, address, money, room_area, room_num)
                except Exception as e:
                    print("解析出现错误,跳过本条数据")
                    continue
            print("本页保存了"+str(count)+"条数据")


    def save_data(self,title,address,money,room_area,room_num):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS, database=self.MYSQL_DB,charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "INSERT INTO room (id,title,address,money,room_area,room_num) VALUES ( '%s', '%s', '%s' ,'%s', '%s', '%s')"
        value = ('0',title,address,money,room_area,room_num)
        # print(sql % value)
        cur.execute(sql % value)
        connect.commit()


spider = Spilser()
spider.getRoom()