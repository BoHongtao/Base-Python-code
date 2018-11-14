import pymysql.cursors
from lottery import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_CHARACTERS = settings.MYSQL_CHARACTERS
# 获取游标
connect = pymysql.Connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB,charset=MYSQL_CHARACTERS)
cur = connect.cursor()

class Sql:
    @classmethod
    def insert(cls,no,pre1,pre2,pre3,pre4,pre5,heil1,heil2,data):
        sql = "INSERT INTO lottery (id,no,pre1,pre2,pre3,pre4,pre5,heil1,heil2,data) VALUES ( '%s', '%s', '%s' ,'%s', '%s', '%s', '%s' ,'%s', '%s', '%s')"
        value = ('0',no,pre1,pre2,pre3,pre4,pre5,heil1,heil2,data)
        cur.execute(sql % value)
        connect.commit()