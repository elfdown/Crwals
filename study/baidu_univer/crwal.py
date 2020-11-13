import requests
import json
from lxml import etree
import pymysql

def get_url(url,headers,i):#输入页数，url，headers，得到一个
    try :
        url_list = []
        list = {"limit":30,
                "timeout":"3000",
                "filterTags":"[0,0,0,0,0,0,0]",
                "tagId":"60826",
                "fromLemma":"true",
                "contentLength":"38",
                "page":"{}".format(i)}
        r = requests.post(url,headers = headers,data=list,timeout = 30)
        r.raise_for_status()
        jdata = json.loads(r.content)
        for i in jdata["lemmaList"]:
            url_list.append(i["lemmaUrl"])
        return(url_list)         
    except :
        return([])
    
def get_info(url,headers):
    try:
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        tree = etree.HTML(r.text)
        zname = "".join(tree.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()"))
        ename = "".join(tree.xpath("//dd[@class='lemmaWgt-lemmaTitle-subTitle']//h3/text()"))
        surl = "".join(tree.xpath("//div[@class='baseBox']/div[2]//dl[@class=' bottomLine']/dd/a/text()"))
        info = [zname,ename,surl]
        return (info)
    except:
        return ([])    
    
    
if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0","Referer": "https://baike.baidu.com/wikitag/taglist?tagId=60826&fromLemma=true"}  
    url = "https://baike.baidu.com/wikitag/api/getlemmas"
    url_list = []
    print("正在存储高校链接……")
    for i in range(5):
        url_list += get_url(url,headers,i)
        
    print("正在连接数据库……")
    try:
        con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",charset="utf8")
        cursor = con.cursor()
        cursor.execute("use baidu")
        print("连接成功")
    except:
        print("连接失败")
    print("正在写入信息……")
    for index,url in enumerate(url_list):
        try:
            info = get_info(url,headers)
            cursor.execute("INSERT INTO good_university (id,zname,ename,surl)VALUE ({},'{}','{}','{}')".format(index+1,info[0],info[1],info[2]))
            print("已完成{}条记录".format(index+1))
            if not ((index+1) % 20):
                con.commit()
        except:
            print("第{}条记录写入失败".format(index+1))
    con.commit()
    print("写入信息完毕！")
        