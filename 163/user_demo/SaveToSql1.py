import pymysql
import getInfo_grequests
import os
import json
import time


conn=pymysql.connect(host='212.64.6.2',port=3306,user='myuser',passwd='dzt',db='sov',charset="utf8")
cursor=conn.cursor()
def GetUserId(i):    
    sql='select user_id from comment where id between'
    cursor.execute(sql+' {} and {}'.format(i*1000,(i+1)*1000))
    result=cursor.fetchall()
    result=tuple(set(result))
    return result
    print(result)
# for i in result:    
#     Info=getInfo.GetUserInfo(i[0])
#     print(i,Info)
def getUserInfos(i):
    result=GetUserId(i)
    step = 100
    UserIdsGroup =[result[i:i+step] for i in range(0,len(result),step)]
    AllUserInfo=[]
    for UserIds in UserIdsGroup:    
        UserIds=[i[0] for i in UserIds]
        texts=getInfo_grequests.getText(UserIds)
        for i in range(len(UserIds)):
            UserInfo=getInfo_grequests.GetUserInfo(texts[i])
            print(i,UserInfo)
            if UserInfo!=0:
                AllUserInfo.append(UserInfo)
    return AllUserInfo
# start=time.time()
# getUserInfos(1)
# end=time.time()
# print(end-start)
# print(AllUserInfo)
def SavetoSql(i):
    data=getUserInfos(i)    
    sql="INSERT INTO user(user_id,user_name,level,sex,age,province,city,fan_count,follow_count,listen_count,user_url)\
        VALUES("+"%s,"*10+"%s)"
    #print(sql)
    cursor.executemany(sql,data)
    conn.commit()

SavetoSql(1)