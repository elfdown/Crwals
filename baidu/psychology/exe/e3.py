import json
import requests
import pymysql
from lxml import etree
import os
url = "https://bkimg.cdn.bcebos.com/pic/ac6eddc451da81cb2fac00e55f66d0160924314b.png"
headers = { "Host": "baike.baidu.com",\
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
            "Referer": "https://baike.baidu.com/wikitag/taglist?tagId=76606"
            }
r = requests.get(url,headers = headers,timeout = 30)
r.raise_for_status()
path = "/Users/downing/Documents/Crwalbugs/biadu/psychology/images/test.jpg"
with open(path,"wb") as f:
    f.write(r.content)