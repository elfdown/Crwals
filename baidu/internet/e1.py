import requests
import json
import time
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = "H485LH3Y23N6X1ND"
proxyPass = "D66C51DE9EA2B31F"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
"host" : proxyHost,
"port" : proxyPort,
"user" : proxyUser,
"pass" : proxyPass,
}
proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}

url = "https://baike.baidu.com/wikitag/api/getlemmas"
headers = { "Host": "baike.baidu.com",\
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",\
            "Accept": "application/json, text/javascript, */*; q=0.01",\
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
            "Accept-Encoding": "gzip, deflate, br",\
            "Referer": "https://baike.baidu.com/wikitag/taglist?tagId=76607",\
            "Cookie":"BAIDUID=6E189BDB1C73D0DA3DA8BBC235CA6545:FG=1; BIDUPSID=\
                6E189BDB1C73D0DA3DA8BBC235CA6545; PSTM=1568510595; MCITY=289-289\
                %3A; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1586615139,1586615319,\
                1586616100,1586736715; BK_SEARCHLOG=%7B%22key%22%3A%5B%221989%E5%B9%B4%\
                22%2C%221840%E5%B9%B4%22%2C%22%E8%A6%86%E7%9B%96%22%2C%22MAC%E5%9C%B0%E5%\
                9D%80%22%2C%22MTU%22%2C%22%E7%8E%8B%E6%A2%93%E9%91%AB%22%2C%22%E5%8F%8C%E5%\
                B0%84%E7%9A%84%E8%8B%B1%E6%96%87%E8%A1%A8%E8%BE%BE%22%2C%22%E5%B9%BF%E4%B9%8\
                9%E4%BA%8C%E9%A1%B9%E5%BC%8F%E5%AE%9A%E7%90%86%22%2C%22%E5%91%BD%E9%A2%98%E5%8\
                F%98%E9%A1%B9%E4%B8%80%E5%AE%9A%E6%98%AF%E5%8E%9F%E5%AD%90%E5%91%BD%E9%A2%98%E4%B9%88%22%5D%7D"
            }
            
def get_info(url,headers,data,proxies,times = 0):#输入请求的URL，headers，data，得到一个名字和url信息的列表
    try:
        infolist = []
        c = requests.get("http://icanhazip.com",proxies = proxies)
        print(c.text)
        r = requests.post(url,headers = headers,data = data,proxies = proxies,timeout = 30)
        r.raise_for_status()
        jdata = json.loads(r.content)
        for i in jdata["lemmaList"]:
            info = [i["lemmaId"],i["lemmaTitle"].replace("'",""),i["lemmaUrl"]]
            infolist.append(info)
        return(infolist)
    except:
        if times == 3:
            print("return failed")
            return([[],[],[]])
        else:
            times += 1
            print("try NO.{} connection".format(times))
            return(get_info(url,headers,data,proxies,times))#尝试断线重连
            
if __name__ == "__main__":
    print("writing in data ...")
    url_index = 12036
    for i in range(500,666):
        data = {"limit":"24",\
                "timeout":"3000",\
                "filterTags":"[]",\
                "tagId":"76607",\
                "fromLemma":"false",\
                "contentLength":"40",\
                "page":"{}".format(i)
                }
        info_list = get_info(url,headers,data,proxies)
        time.sleep(2)
        print(info_list[0])
            