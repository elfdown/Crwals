import requests
import os

root = "/Users/downing/Documents/GitHub/Tcode/EXE/EE/pic/"
url = "https://www.cgtn.com/video"
pic_name = os.path.split(url)[-1]
path = os.path.join(root,pic_name)
u_a = {"Uer-Agent":"Mozilla5.0"}

try:
    if not os.path.exists(path):
        r = requests.get(url,headers = u_a,timeout = 30)
        print(r.status_code)
        with open(path,"wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    
print(path)