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

def get_top50_song(artist_ids, songids):
  entrance = 'https://music.163.com/artist'
  for artist_id in artist_ids:
    data = {'id':artist_id}
    tree = get_tree(entrance, tpl_h, data)
    hrefs = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    for href in hrefs:
      songid = re.findall(r'\d+$',href)
      songids.append(songid[0])

def get_artists(urlnums):
  entrance = "https://music.163.com/discover/artist/cat"
  idlist = ['1','2','4','6','7']
  initid = [0]
  for i in range(65, 91):
    initid.append(i)
  data = {'id': 1}
  for _id in idlist:
    cir = ['1','2','3']
    for __id in cir:
      catid = _id + '00' + __id
      data['id'] = catid
      for alp in initid:
        data['initial'] = alp
        tree = get_tree(entrance, tpl_h, data)
        arturls1 = tree.xpath('//li[@class="line"]//a[1]/@href')
        arturls2 = tree.xpath('//li[@class="sml"]/a[1]/@href')
        for href in arturls1:
          urlnum = re.findall(r'\d+$',href)
          urlnums.append(urlnum[0])
        for href in arturls2:
          urlnum = re.findall(r'\d+$',href)
          urlnums.append(urlnum[0])

def get_contents(songids, dataset):
  scp = song_commment_api = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
  url = "https://music.163.com/song"
  count = 0
  for songid in songids:
    count += 1
    comment_datalist = []
    song_datalist = []
    metadata = [count, songid, comment_datalist, song_datalist]

    r = requests.get(scp, timeout=10, headers=tpl_h)
    r.raise_for_status()
    rdata = json.loads(r.content)
    
    counter = 0
    for comment in rdata['hotComments']:
      counter += 1
      comment_datalist.append([counter, comment['time'], comment['likedCount'], comment['content'], comment['user']['userId']])
    metadata.append(comment_datalist)

    data = {'id':songid}
    tree = get_tree(url, tpl_h, data)
    artist = tree.xpath('//p[@class="des s-fc4"][1]//a/text()')[0]
    album = tree.xpath('//p[@class="des s-fc4"][2]//a/text()')[0]
    songname = tree.xpath('//em[@class="f-ff2"]/text()')[0]
    song_datalist.append([artist, album, songname])
    metadata.append(song_datalist)
    dataset.append(metadata)

artids=[]
get_artists(artids)
songids=[]
get_top50_song(artids,songids)
dataset=[]
get_contents(songids, dataset)