import json
import requests
import pymysql

def get_info(url,headers,data,times = 0):#输入请求的URL，headers，data，得到一个名字和url信息的列表
    try:
        infolist = []
        r = requests.post(url,headers = headers,data = data,timeout = 30)
        r.raise_for_status()
        jdata = json.loads(r.content)
        for i in jdata["lemmaList"]:
            if i["lemmaPic"] == []:
                info = [i["lemmaId"],i["lemmaTitle"].replace("'",""),i["lemmaUrl"],""]
            else:
                info = [i["lemmaId"],i["lemmaTitle"].replace("'",""),i["lemmaUrl"],i["lemmaPic"]["url"]]
            infolist.append(info)
        return(infolist)
    except:
        if times == 3:
            print("return failed")
            return([[],[],[],[]])
        else:
            times += 1
            print("try NO.{} connection".format(times))
            return(get_info(url,headers,data,times))#尝试断线重连

if __name__ == "__main__":
    
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
    info_list = get_info(url,headers,data)
    print(info_list[3])