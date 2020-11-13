import json
import requests
import pymysql
import time

def get_info(url,headers,data,times = 0):#输入请求的URL，headers，data，得到一个名字和url信息的列表
    try:
        infolist = []
        r = requests.post(url,headers = headers,data = data,timeout = 30)
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
            return(get_info(url,headers,data,times))#尝试断线重连

if __name__ == "__main__":
    
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
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
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
                "Accept": "application/json, text/javascript, */*; q=0.01",\
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
                "Accept-Encoding": "gzip, deflate, br",\
                "Referer": "https://baike.baidu.com/wikitag/taglist?tagId=76607"
                }
    try:
        con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",charset="utf8")
        cursor = con.cursor()
        cursor.execute("use baidu")
        con.commit()
        print("database connecting succeeded!")
    except:
        print("database connecting failed!")
    else:
        print("writing in data ...")
        url_index = 12036
        for i in range(500,666):
            try:
                data = {"limit":"24",\
                        "timeout":"3000",\
                        "filterTags":"[]",\
                        "tagId":"76607",\
                        "fromLemma":"false",\
                        "contentLength":"40",\
                        "page":"{}".format(i)
                        }
                info_list = get_info(url,headers,data)
                for info in info_list:
                    url_index += 1
                    cursor.execute("INSERT INTO internet_url (id,baidu_id,keyname,keyurl) \
                                    VALUE ({},{},'{}','{}')".format(url_index,info[0],info[1],info[2]))
                con.commit()
                print("page NO.{} done!".format(i+1))
            except:
                print("page NO.{} failed!".format(i+1))
        print("all done!")

                
    
    
