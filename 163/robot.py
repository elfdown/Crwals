import requests
from lxml import etree

r = requests.get("https://www.xiami.com/song/U8wwjH2930c")
r.raise_for_status()
r.encoding = r.apparent_encoding
tree = etree.HTML(r.text)
print(tree.xpath("//div[@class = 'lyric-content']//text()"))
print(tree.xpath("//div[@class= 'button unselectable']//text()"))