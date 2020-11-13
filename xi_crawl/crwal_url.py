import requests
from lxml import etree
import json

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113'}
url_0 = 'http://jhsjk.people.cn/result'
k = 8
ran = 8
data = {'type':100+k}
urls = []
for i in range(1,ran+1):
    url = url_0+'/{}'.format(i)
    r = requests.get(url,headers=headers,timeout=30,params=data)
    r.encoding=r.apparent_encoding
    tree=etree.HTML(r.text)
    href_list = tree.xpath("//li/a[@target='_blank']/@href")
    urls += href_list
    print(i)
    
with open('./urls/10{}.json'.format(k),'w') as f:
    json.dump(urls,f)