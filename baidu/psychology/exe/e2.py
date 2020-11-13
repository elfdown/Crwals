import requests

url = "http://baike.baidu.com/item/%E8%AF%8D%E8%AF%AD%E6%B7%B7%E4%B9%B1/22308706"
headers = { "Host": "baike.baidu.com",\
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
        "Accept": "application/json, text/javascript, */*; q=0.01",\
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
        "Accept-Encoding": "gzip, deflate, br",\
        "Referer": "https://baike.baidu.com/wikitag/taglist?tagId=76606"
        }
r = requests.get(url,headers = headers)
with open ("test.html","wb") as f:
    f.write(r.content)