from bs4 import BeautifulSoup
import requests
import pymysql.cursors

class Spilser:
    MYSQL_HOSTS = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_PORT = '3306'
    MYSQL_DB = 'room'
    MYSQL_CHARACTERS = 'utf8'
    base_url = "https://jn.zu.anjuke.com/fangyuan/p"
    headers = {
        'Connection': 'keep-alive',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    def getRoom(self):
        for i in range(1,50):
            url = self.base_url+str(i)+"/"
            print("访问的url"+url)
            response = requests.get(url,headers=self.headers).text
            rooms = BeautifulSoup(response,'lxml').findAll('div',class_='zu-itemmod')
            count = 0
            for room in rooms:
                # print(room)
                # 标题
                title = room.find('div',class_='zu-info').find('h3').find('a')['title']
                # 房间基本信息
                room_info  = room.find('p',class_='details-item tag').get_text().strip().split('|')
                room_num = room_area = room_level = room_owner = ''
                if len(room_info)==3:
                    room_num = room_info[0]
                    room_area = room_info[1]
                    room_level = room_info[2].split('\ue147')[0]
                    room_owner = room_info[2].split('\ue147')[1]
                if len(room_info)==4:
                    room_num = room_info[0]
                    room_area = room_info[1]
                    room_level = room_info[2]
                    room_owner = room_info[3]
                # 出租方式
                type = room.find('span',class_='cls-1').get_text()
                # 朝向
                toward = room.find('span',class_='cls-2').get_text()
                # 价格
                price = room.find('div',class_='zu-side').find('p').get_text()
                self.save_data(title,room_num,room_area,room_level,room_owner,type,toward,price)
                count = count + 1
            print("保存第"+str(i)+"页数据数据成功,数据条数"+str(count))
                # exit()

    def save_data(self,title,room_num,room_level,room_area,room_owner,type,toward,price):
        # 获取游标
        connect = pymysql.Connect(user=self.MYSQL_USER, password=self.MYSQL_PASSWORD, host=self.MYSQL_HOSTS, database=self.MYSQL_DB,charset=self.MYSQL_CHARACTERS)
        cur = connect.cursor()
        sql = "INSERT INTO room (id,title,room_num,room_area,room_level,room_owner,type,toward,price) VALUES ( '%s', '%s', '%s' ,'%s', '%s', '%s', '%s', '%s','%s')"

        value = ('0', title, room_num, room_area,room_level, room_owner, type,toward,price)
        print(sql % value)
        cur.execute(sql % value)
        connect.commit()

spider = Spilser()
spider.getRoom()