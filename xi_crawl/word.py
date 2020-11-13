import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pymysql
import time
import datetime
import jieba.analyse
import json
from analyze import sqlDocAnalyze
import numpy as np

con = pymysql.connect(host='127.0.0.1',port=3306,user='root',db='xi',charset="utf8mb4")
cursor = con.cursor()
t1_list = ['经济','政治','文化','社会','生态','党建','国防','外交']
t2_list = ['原文','会议','活动','考察','会见','出访','讲话','函电']
# t = t1_list[0]
# cursor.execute('SELECT * from `type1` where `type` = "{}"'.format(t))
cursor.execute('SELECT * from `type1`')
result = cursor.fetchall()
book = sqlDocAnalyze(result)
book.saveByIndex('test.txt',4)
doc = book.doc(4)

text = doc['text']
text = text.replace('\n',"").replace("\u3000","")
text_cut = jieba.lcut(text)
text_cut = ' '.join(text_cut)
stop_words = open("stop_words.txt",encoding="utf8").read().split("\n")
# 主要区别
background = Image.open("background.jpg")
graph = np.array(background)

word_cloud = WordCloud(font_path="SweiSpringSugarCJKtc-Regular.ttf", 
                       background_color="white", 
                       mask=graph, # 指定词云的形状
                       stopwords=stop_words)

word_cloud.generate(text_cut)
plt.subplots(figsize=(12,8))
plt.imshow(word_cloud)
plt.axis("off")