import json
import requests
import pymysql

con = pymysql.connect(host="127.0.0.1",db="baidu",port=3306,user="root",password="",charset="utf8")
cursor = con.cursor()
cursor.execute("SELECT * FROM psychology_url where id= 1")
for i,url_tuple in enumerate(cursor.fetchall()):
    print(i)
    print(url_tuple[0])
    print(url_tuple[1])