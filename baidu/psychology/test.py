import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
    }
url = "https://news.sjtu.edu.cn/jdyw/20200622/126197.html"


r = requests.get(url=url,headers = headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
tree = etree.HTML(r.text)

p = tree.xpath("//p//text()")




