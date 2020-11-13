import getRecords
import pymysql

conn=pymysql.connect(host='212.64.6.2',port=3306,user='myuser',passwd='dzt',db='sov',charset="utf8")
cursor=conn.cursor()
def GetUserId(i):    
    sql='select user_id from user where id between'
    cursor.execute(sql+' {} and {}'.format(i*100+1,(i+1)*100))
    result=cursor.fetchall()
    #result=tuple(set(result))
    print(result)
    return result

def SaveToSql(i):    
    result=GetUserId(i)
    UserRecords=[]
    count=i*100+1
    for i in result:
        UserRecord=getRecords.getRecords(i[0])
        print(UserRecord)
        if UserRecord!=0:
            index=(count,)
            UserRecord=UserRecord+index
            UserRecords.append(UserRecord)
        count+=1
    cursor.executemany("UPDATE user SET record_song=%s,record_artist=%s WHERE Id=%s",UserRecords)
    conn.commit()
SaveToSql(0)