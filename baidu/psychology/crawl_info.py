import json
import requests
import pymysql
from lxml import etree
import os

# def save_img(url,root,keyid,headers,times = 0):#给出路径的根，和图片的网络链接，将图片存储在本地，并返回一个相对路径
    
#     if url == "" :
#         return("")
    
#     pic_name = url[33:]
#     path = os.path.join(root,pic_name)

#     try:
#         if not os.path.exists(path):
#             print(1)
#             r = requests.get(url,headers = headers,timeout = 30)
#             r.raise_for_status()
#             print(1)
#             with open(path,"wb") as f:
#                 f.write(r.content)
#         return("images/{}".format(pic_name))
#     except:
#         if times == 3:
#             print("pic_path {} return failed".format(keyid))
#             return("")
#         else:
#             times += 1
#             print("try NO.{} connection".format(times))
#             return(save_img(url,root,id,headers,times))#尝试断线重连
    
def count_discussion(headers,baidu_id,keyid,times = 0):
    discussion_url = "https://baike.baidu.com/discussion/api/getdiscussioncount?lemmaId={}".format(baidu_id)
    try:
        r = requests.get(discussion_url,headers=headers)
        r.raise_for_status()
        jdata = json.loads(r.content)
        discussion_count = jdata["data"]["discussionCount"]
        return discussion_count
    except:
        if times == 3:
            print("discussion_count {} return failed".format(keyid))
            return(-1)
        else:
            times += 1
            print("try NO.{} connection".format(times))
            return(count_discussion(headers,baidu_id,keyid,times))#尝试断线重连
    
def count_share(headers,baidu_id,keyid,times = 0):
    sharecounter_url = "https://baike.baidu.com/api/wikiui/sharecounter?lemmaId={}&method=get".format(url_tuple[1])
    try:
        r = requests.get(sharecounter_url,headers=headers)
        r.raise_for_status()
        jdata = json.loads(r.content)
        share_count = jdata["shareCount"]
        like_count = jdata["likeCount"]
        return (share_count,like_count)
    except:
        if times == 3:
            print("share_count {} return failed".format(keyid))
            return(-1)
        else:
            times += 1
            print("try NO.{} connection".format(times))
            return(count_share(headers,baidu_id,keyid,times))#尝试断线重连

def get_info(url,headers,keyid,times = 0):#得到一个信息列表
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        tree = etree.HTML(r.text)
        brief_intro = "".join(tree.xpath("//div[@class='lemma-summary']//div//text()"))
        key_words = "".join(tree.xpath("//meta[@name='keywords']/@content"))
        return(brief_intro,key_words)
    except:
        if times == 3:
            print("get_info {} return failed".format(keyid))
            return("","")
        else:
            times += 1
            print("try NO.{} connection".format(times))
            return(get_info(url,headers,keyid,times))#尝试断线重连

if __name__ == "__main__":
    
    root = "/Users/downing/Documents/Crwalbugs/biadu/psychology/images"
    
    con = pymysql.connect(host="127.0.0.1",db="baidu",port=3306,user="root",password="",charset="utf8")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM psychology_url")
    
    for url_tuple in cursor.fetchall():
        #url_tuple:(id,baidu_id,keyname,keyurl,pic_url)
        
        headers = { "Host": "baike.baidu.com",\
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",\
            "Referer": "{}".format(url_tuple[3])
            }#to change headers
        
        discussion_count = count_discussion(headers,url_tuple[1],url_tuple[0])#int
        share_count,like_count = count_share(headers,url_tuple[1],url_tuple[0])#str,str
        brief_intro,key_words = get_info(url_tuple[3],headers,url_tuple[0])#text,text
        # pic_path = save_img(url_tuple[4],root,url_tuple[0],headers)
        print(discussion_count,share_count,like_count,brief_intro,key_words)
        try:
            cursor.execute("INSERT INTO psychology_info (id,key_name,discussion_count,share_count,like_count,brief_intro,key_words) \
                            VALUE ({},'{}',{},{},{},'{}','{}')".format(url_tuple[0],url_tuple[2],discussion_count,share_count,like_count,brief_intro,key_words))
        except:
            print("No {} failed".format(url_tuple[0]))
            
        if not url_tuple[0] % 10 :
            con.commit()
            print("No.{} url done".format(url_tuple[0]))
    
    con.commit()
    print("all done")
        