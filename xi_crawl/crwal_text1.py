import pymysql
import json
import requests
from lxml import etree
import re

con = pymysql.connect(host='127.0.0.1',port=3306,user='root',db='xi',charset="utf8mb4")
cursor=con.cursor()

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113'}
root = 'http://jhsjk.people.cn/'
t1_list = ['经济','政治','文化','社会','生态','党建','国防','外交']
t2_list = ['原文','会议','活动','考察','会见','出访','讲话','函电']
for i in range(8,9):
    with open ('./json/10{}.json'.format(i)) as f:
        url_list = json.load(f)
    for url_0 in url_list:
        url = root + url_0
        try:
            r = requests.get(url=url,headers=headers,timeout=10)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            tree = etree.HTML(r.text)
            title = ''.join(tree.xpath('//h1/text()'))
            front = ''.join(tree.xpath('//div[@class="d2txt_1 clearfix"]/text()'))
            time = front.split(' ')[-1][-10:]
            source = front.split(' ')[0][3:]
            editor = ''.join(tree.xpath('//div[@class="editor clearfix"]/text()'))
            text = ''.join(tree.xpath('//p//text()'))
            length = len(text)
            article_id = url_0[8:]
            
            t = t1_list[i-1]
            #t = t2_list[i]
            data = [article_id,t,title,time,source,editor,text,length]
            cursor.execute("INSERT INTO type1 (article_id,type,title,time,source,editor,text,length)\
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",data)
            print(i)
        
        except:#如果错误，打开日志写进错误的链接
            print("{} has something wrong".format(url_0))
            with open("./json/flog.json","r") as f:
                mis = json.load(f)
            mis.append([url_0,i])
            with open("./json/flog.json",'w') as f:
                json.dump(mis,f)
    
    con.commit()
