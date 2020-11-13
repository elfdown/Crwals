import grequests
import json
import time
from lxml import etree
import os

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113'}
path=os.getcwd()
with open(path+"\CityCode.txt",'r',encoding='utf-8')as f:
    CityCode=f.read()
    CityCode=json.loads(CityCode)
def ConvertBirthday(birthday):
    # 利用localtime()函数将时间戳转化成时间数组
    localtime = time.localtime(birthday)
    #print(localtime)
    # 利用strftime()函数重新格式化时间
    dt = time.strftime('%Y:%m:%d %H:%M:%S',localtime)
    return dt
    #print(dt)

def GetUserInfo(text):
    try:    
        
        result=json.loads(text)
        UserId=result['userPoint']['userId']
        level=result['level']
        birthday=result['profile']['birthday']
        province=result['profile']['province']
        city=result['profile']['city']
        gender=result['profile']['gender']#1为男2为女0为未知
        followed=result['profile']['followeds']
        follows=result['profile']['follows']
        nickname=result['profile']['nickname']
        listenSongs=result['listenSongs']
        if birthday>0:
            birthday=ConvertBirthday(birthday/1000)
            age=2020-int(birthday[:4])
        else:
            age=0
        #path=os.getcwd()
        # with open(path+"\CityCode.txt",'r',encoding='utf-8')as f:
        #     CityCode=f.read()
        #     CityCode=json.loads(CityCode)
        #print(type(CityCode))
        if str(city) in CityCode:
            city=CityCode[str(city)]
            province=CityCode[str(province)]
        else:
            city='海外'
            province='海外'
        user_url='https://music.163.com/user/home?id='+str(UserId)
        # print(province)
        # print(city)
        # print(gender)
        # print(level,nickname,listenSongs)
        # print(followed,follows)
        #print(age)
        return(UserId,nickname,level,gender,age,province,city,followed,follows,listenSongs,user_url)
    except:
        return 0
def getText(UserIds):
    reqs=[]
    for i in UserIds:
        url='https://music.163.com/api/v1/user/detail/'+str(i)
        reqs.append(grequests.get(url,headers=headers))

    resultInfos=[]    
    res_list=grequests.map(reqs)    
    res_text_list=[ret.text for ret in res_list if ret and ret.status_code == 200]
    return res_text_list