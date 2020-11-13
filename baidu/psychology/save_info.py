import json
import pymysql

con = pymysql.connect(host="127.0.0.1",db="baidu",port=3306,user="root",password="",charset="utf8")
cursor = con.cursor()
cursor.execute("SELECT * FROM psychology_info")
resualts = cursor.fetchall()
content = []
for resualt in resualts:
    print(resualt)
    dic = {
        "序号":"{}".format(resualt[0]),
        "词条名":"{}".format(resualt[1]),
        "讨论数":"{}".format(resualt[2]),
        "分享数":"{}".format(resualt[3]),
        "喜欢数":"{}".format(resualt[4]),
        "简介":"{}".format(resualt[5]),
        "关键词":"{}".format(resualt[6]),
    }
    print(dic)
    content.append(dic)
    
with open ("./baidu/psychology/info.json","w") as f:
    json.dump(content,fp = f,ensure_ascii = False, indent = 4)