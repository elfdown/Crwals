import pymysql
import time
import datetime
import jieba
import jieba.analyse
import json
from analyze import sqlDocAnalyze

def json_print(json_dict):
    json_dict = json.dumps(json_dict,indent=4,separators=(',',':'),ensure_ascii=False)
    print(json_dict)
    return

con = pymysql.connect(host='127.0.0.1',port=3306,user='root',db='xi',charset="utf8mb4")
cursor = con.cursor()
t1_list = ['经济','政治','文化','社会','生态','党建','国防','外交']
t2_list = ['原文','会议','活动','考察','会见','出访','讲话','函电']
# t = t1_list[0]
# cursor.execute('SELECT * from `type1` where `type` = "{}"'.format(t))
cursor.execute('SELECT * from `type1`')
result = cursor.fetchall()
book = sqlDocAnalyze(result)

t = '总体'

with open ('./keywords1/{}.txt'.format(t),'w') as f:
    f.write('these are the keywords in type:"{}"\n\n\n'.format(t))
    s = 0
    for i in range(1,11):
        date1 = 20100101+i*10000
        date2 = 20100101+(i+1)*10000
        lis = book.startisticWordByDate(date1,date2)
        tup = lis[0]
        total = lis[1]
        s += total
        for info in tup:
            f.write('keywords:{0:{2}<8}weight:{1}\n'.format(info[0],info[1],chr(12288)))
        f.write('there are {} articles in total\n'.format(total))
        f.write('\n\n{}-{}-{}\n\n\n'.format(str(date2)[:4],str(date2)[4:6],str(date2)[6:]))
        print(0)
        
    f.write('there are {} articles in total in this type\n'.format(s))