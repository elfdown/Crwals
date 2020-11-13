import requests
from bs4 import BeautifulSoup
import bs4

def getUrlText(url):
    """
    输入给定链接，返回页面文本
    """
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return(r.text)
    except:
        print("请求网页异常")
        return("")
    
def getDataIn(the_text):
    """
    输入页面文本，返回一个包含大学信息的列表
    """
    u_list=[]
    soup = BeautifulSoup(the_text,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            u_list.append([tds[0].string,tds[1].string,tds[2].string])
    return(u_list)
        
def printTheData(the_list,num):
    """
    输入列表和要打印的行数，打印值
    """
    mo_ban = "{0:<10}{1:{3}<20}{2:<10}"
    print(mo_ban.format("中国排名","大学名称","世界排名",chr(12288)))
    for i in range(num):
        print(mo_ban.format(the_list[i][0],the_list[i][1],the_list[i][2],chr(12288)))
        
def main():
    url = "http://www.zuihaodaxue.com/World-University-Rankings-2019/China.html"
    the_text = getUrlText(url)
    the_list = getDataIn(the_text)
    printTheData(the_list,100)
    
main()
