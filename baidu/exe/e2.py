import json
import requests
import pymysql

url = "https://baike.baidu.com/wikitag/api/getlemmas"
headers = { "Host": "baike.baidu.com",\
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
            "Accept": "application/json, text/javascript, */*; q=0.01",\
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
            "Accept-Encoding": "gzip, deflate, br",\
            "Referer": "https://baike.baidu.com/wikitag/taglist?tagId=76606"
            }
data = {"limit":"24",\
        "timeout":"3000",\
        "filterTags":"[]",\
        "tagId":"76606",\
        "fromLemma":"false",\
        "contentLength":"40",\
        "page":"{}".format(0)
        }

url_dict = {}
r = requests.post(url,headers = headers,data = data,timeout = 30)
r.raise_for_status()
jdata = json.loads(r.content)
for i in jdata["lemmaList"]:
    url_dict = dict(url_dict,**{i["lemmaTitle"]:i["lemmaUrl"]})
print(url_dict)
con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",charset="utf8")
cursor = con.cursor()
cursor.execute("use baidu")
url_index = 0
for name in url_dict:
    url_index += 1
    print(name)
    print(url_dict[name])
    cursor.execute("INSERT INTO psychology_url (id,keyname,keyurl) \
                    VALUE ({},'{}','{}')".format(url_index,name,url_dict[name]))
    con.commit()