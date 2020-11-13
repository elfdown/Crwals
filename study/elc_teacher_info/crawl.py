import requests
import json
from lxml import etree
import pymysql
import os

def save_img(url,root,headers):#给出路径的根，和图片的网络链接，将图片存储在本地，并返回一个相对路径
    pic_name = os.path.split(url)[-1]
    root = root + "image/"
    path = os.path.join(root,pic_name)

    try:
        if not os.path.exists(path):
            r = requests.get(url,headers = headers,timeout = 30)
            r.raise_for_status()
            with open(path,"wb") as f:
                f.write(r.content)
                f.close()
        return("image/{}".format(pic_name))
    except:
        return("image/")

def get_url(url,headers):#输入页面url，加入headers，得到一个教师的url列表
    try :
        url_list = []
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        tree = etree.HTML(r.text)
        for i_url in tree.xpath("//div[@class='TeacherName']//@href"):
            i_url = "http://www.yingcai.uestc.edu.cn/"+i_url[3:]
            url_list.append(i_url)
        return(url_list)         
    except :
        return([])
    
def get_info(url,headers,root):#输入教师信息的url，网页的headers，图片储存的路径，储存图片，并得到教师的一个信息列表
 
    try:
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        tree = etree.HTML(r.text)
        zname = "".join(tree.xpath("//div[@class='TeacherDes ClearFix']/img/@alt"))
        img_url = "http://www.yingcai.uestc.edu.cn"+"".join(tree.xpath("//div[@class='TeacherDes ClearFix']/img/@src"))
        img = save_img(img_url,root,headers)
        title = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[1]/span[1]/text()'))[3:]
        team = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[1]/span[2]/text()'))[3:]
        work_phone = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[1]/span[3]/text()'))[5:]
        ace_quali = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[2]/span[1]/text()'))[3:]
        positon = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[2]/span[2]/text()'))[3:]
        email = "".join(tree.xpath('//div[@class="TeacherDesWrapperSub"]/div[2]/span[3]/text()'))[3:]
        detail_list = tree.xpath('//div[@class="TeacherInfoDetail"]/p[1]/text()')
        info = [zname,img,title,team,work_phone,ace_quali,positon,email]+detail_list
        if len(info) < 12:
            while len(info) < 12:
                info.append("")
            info[10] = info[8]
            info[8] = ""#对于信息不全的一个简单的补救
        return (info)
    except:
        return ([])
       
if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0)\
         Gecko/20100101 Firefox/74.0",\
        "Referer": "http://www.yingcai.uestc.edu.cn/"}  
    
    url_list = []
    print("正在存储教师信息网页的链接……")
    url = "http://www.yingcai.uestc.edu.cn/szdw/jszy.htm"
    url_list += get_url(url,headers)
    for i in range(3):
        url = "http://www.yingcai.uestc.edu.cn/szdw/jszy/{}.htm".format(i+1)
        url_list += get_url(url,headers)#获得教师链接列表
    
    print("正在连接数据库……")
    try:
        con = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",charset="utf8")
        cursor = con.cursor()
        cursor.execute("use baidu")
        print("连接成功")
    except:
        print("连接失败")#连接数据库
        
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0)\
         Gecko/20100101 Firefox/74.0",\
        "Referer": "http://www.yingcai.uestc.edu.cn/szdw/jszy.htm/"} #更换头部信息
    root = "/Users/downing/Documents/Crwalbugs/study/elc_teacher_info/"#设定图片的存储路径
    
    print("正在写入信息……")
    for index,url in enumerate(url_list):
        try:
            info = get_info(url,headers,root)#获得教师的信息列表并储存图片
            cursor.execute("INSERT INTO elc_teachers_info (id,zname,img,title,\
                team,work_phone,ace_quali,positon,email,teaching_background,\
                research_direction,teaching_course,research_results) VALUE ({},'{}','{}','{}','{}','{}',\
                    '{}','{}','{}','{}','{}','{}','{}')"\
                    .format(index+1,info[0],info[1],info[2],info[3],\
                        info[4],info[5],info[6],info[7],info[8],\
                            info[9],info[10],info[11]))#将数据逐条上传至数据库
            con.commit()
            print("已完成{}条记录".format(index+1))
        except:
            print("第{}条记录写入失败".format(index+1))
    print("写入信息完毕！")