import requests
from lxml import etree
import re
import json
from bs4 import BeautifulSoup


tpl_h = toplist_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                          AppleWebKit/537.36 (KHTML, like Gecko)\
                                          Chrome/80.0.3987.163 Safari/537.36',
                              'Referer': 'https://music.163.com/'}                           

def get_tree(url, headers, data):
  r = requests.get(url, timeout=10, headers=headers, params=data)
  r.raise_for_status()
  r.encoding = r.apparent_encoding
  tree = etree.HTML(r.text)
  return tree

def dump_json_Chinese(address, data, _indent = 0):
  with open(address, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent = _indent, ensure_ascii=False)

def get_albums(album_ids, artid):
  data = {'id':artid, 'limit':600, 'offset':0}
  tree = get_tree('https://music.163.com/artist/album', tpl_h, data)
  a_s = tree.xpath('//p[@class="dec dec-1 f-thide2 f-pre"]/a')
  for element in a_s:
    href = element.xpath('./@href')
    text = element.xpath('./text()')
    urlnum = re.findall(r'\d+$',href[0])
    album_ids.append( {urlnum[0]:text[0]} )

with open(r'D:\scrapy codes\artist_ids copy.json','r',encoding='utf8')as fp:
  artist_ids = json.load(fp)
album_ids = []
for artist_id in artist_ids:
  get_albums(album_ids, artist_id)

################################
##get_albums(album_ids, 7763)
#
#for artist_id in artist_ids:
#  get_albums(album_ids, artist_id)
#
################################

address = r'D:\scrapy codes\data\album\album_ids.json'
dump_json_Chinese(address, album_ids)