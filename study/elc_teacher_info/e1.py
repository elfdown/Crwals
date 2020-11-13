import requests
import json
from lxml import etree
import pymysql

def get_url(url,headers):#输入页数，url，headers，得到一个
    try :
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        tree = etree.HTML(r.text)
        print(len(tree.xpath('//div[@class="TeacherInfoDetail"]/p[1]/text()')))        
    except :
        print("wrony")
    
    
if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
        "Referer": "http://www.yingcai.uestc.edu.cn/"}  
    url = "http://www.yingcai.uestc.edu.cn/info/1018/1888.htm"
    get_url(url,headers)