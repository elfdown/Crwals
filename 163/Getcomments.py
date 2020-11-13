import grequests
import requests
import json
from lxml import etree
import time
import random
import pymysql

conn=pymysql.connect(host='212.64.6.2',port=3306,user='myuser',passwd='dzt',db='sov',charset="utf8")
cursor=conn.cursor()

def ConvertBirthday(birthday):
    # 利用localtime()函数将时间戳转化成时间数组
    localtime = time.localtime(birthday)
    #print(localtime)
    # 利用strftime()函数重新格式化时间
    dt = time.strftime('%Y:%m:%d %H:%M:%S',localtime)
    return dt

def GetHotsongs(artist_id):
    url='https://music.163.com/artist?id='+str(artist_id)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36','referer':'https://music.163.com/'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    info=tree.xpath('//textarea[@id="song-list-pre-data"]/text()')
    jobj = json.loads(info[0])
    ids=[]
    for item in jobj:
        ids.append(item['id'])
    return ids
    



def spider_comment(id,artistid):
    url1='http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(id)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    
    reqs=[]
    for i in range(0,1000,20):
        params={'limit':20,'offset':i}
        reqs.append(grequests.get(url1,headers=headers,params=params))
        
    res_list=grequests.map(reqs)    
    res_text_list=[ret.text for ret in res_list if ret and ret.status_code == 200]
    for r in res_text_list:    
        result=json.loads(r)
        #print(result)
        data=[]
        for i in result['comments']:
            commentId=i['commentId']
            comments=i['content']
            like=i['likedCount']
            userId=i['user']['userId']
            time=ConvertBirthday(i['time']/1000)
            tmp=[commentId,comments,id,artistid,time,like,userId]
            data.append(tmp)
        
        cursor.executemany("INSERT INTO comment(comment_id,content,song_id,artist_id,create_time,like_count,user_id)\
            VALUES(%s,%s,%s,%s,%s,%s,%s)",data)
    conn.commit()


if __name__ == "__main__":
    
    with open("running.json","r+") as f:
        cr = json.load(f)
    
    for artist_id in cr:
        try:#尝试爬取
            ids=GetHotsongs(artist_id)
            for id in ids[:20]:
                spider_comment(id,artist_id)
                print("{}song completed".format(id))
                time.sleep(1)
                
        except:#如果错误，打开日志写进错误的歌手id
            print("{} has something wrong".format(artist_id))
            with open("mistake.json","r") as f:
                mis = json.load(f)
            mis.append(artist_id)
            print(mis)
            with open("mistake.json",'w') as f:
                json.dump(mis,f)
        
        with open("running.json", 'r') as f:
            lis = json.load(f)
        lis = lis[1:]
        with open("running.json",'w') as f:
            json.dump(lis,f)
            
        print("{} artist completed".format(artist_id))