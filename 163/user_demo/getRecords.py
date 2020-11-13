import requests
import math
import random
# pycrypto
from Crypto.Cipher import AES
import codecs
import base64
import json


# 构造函数获取歌手信息
def get_comments_json(url, data):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Connection': 'keep-alive',
             'Host': 'music.163.com',
             'Referer': 'http://music.163.com/',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/66.0.3359.181 Safari/537.36'}

    try:
        r = requests.post(url, headers=headers, data=data)
        r.encoding = "utf-8"
        if r.status_code == 200:

            # 返回json格式的数据
            return r.json()

    except:
        print("爬取失败!")


# 生成16个随机字符
def generate_random_strs(length):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # 控制次数参数i
    i = 0
    # 初始化随机字符串
    random_strs  = ""
    while i < length:
        e = random.random() * len(string)
        # 向下取整
        e = math.floor(e)
        random_strs = random_strs + list(string)[e]
        i = i + 1
    return random_strs


# AES加密
def AESencrypt(msg, key):
    # 如果不是16的倍数则进行填充(paddiing)
    padding = 16 - len(msg) % 16
    # 这里使用padding对应的单字符进行填充
    msg = msg + padding * chr(padding)
    # 用来加密或者解密的初始向量(必须是16位)
    iv = '0102030405060708'
    #print(type(key),type(iv))
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    # 加密后得到的是bytes类型的数据
    encryptedbytes = cipher.encrypt(msg.encode())
    # 使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf-8')

    return enctext


# RSA加密
def RSAencrypt(randomstrs, key, f):
    # 随机字符串逆序排列
    string = randomstrs[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    seckey = int(codecs.encode(text, encoding='hex'), 16)**int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)


# 获取参数
def get_params(id):
    # msg也可以写成msg = {"offset":"页面偏移量=(页数-1) *　20", "limit":"20"},offset和limit这两个参数必须有(js)
    # limit最大值为100,当设为100时,获取第二页时,默认前一页是20个评论,也就是说第二页最新评论有80个,有20个是第一页显示的
    # msg = '{"rid":"R_SO_4_1302938992","offset":"0","total":"True","limit":"100","csrf_token":""}'
    # 偏移量
    
    # offset和limit是必选参数,其他参数是可选的,其他参数不影响data数据的生成
    msg = '{"offset":"0 ","total":"True","limit":"1000","uid":'+str(id)+',"type":"0"}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enctext = AESencrypt(msg, key)
    # 生成长度为16的随机字符串
    i = generate_random_strs(16)

    # 两次AES加密之后得到params的值
    encText = AESencrypt(enctext, i)
    # RSA加密之后得到encSecKey的值
    encSecKey = RSAencrypt(i, e, f)
    return encText, encSecKey

def getRecords(id):
    url='https://music.163.com/weapi/v1/play/record?csrf_token='+str(id)
    params, encSecKey = get_params(id)
    #data = {'params': '9n8nTsH+vLu2OxYt4SRn0DnvO6VPQlLmbry1/VDRl89YjHlkv6LC0wHQdZ9i6YclOHZr9G2Vu16yFg5PAfaPMoyUS1c8kl4poKmwhieYLiQv6WZhXRnxuZ+cCeuhKa8/Lgeh3Uz+/6UNixV7ULZ5dpjEEsP8RJtxb0OqCy3+jSwfjTFXPO8oQI8qYbbbdMJd', 'encSecKey': '9330f0fe87ebde757ab743511c6f686494ac7aa6e565e23c80d4d312c17644ff484ab8ab719d0664b6c1bd6ed3a3cf16af31803eb57f22fcf0575271573b6fe8d11716103295c0685a5de7f134a3b94069fbe9388cf1b3efe3e71d56d4923e81011f0fe10e156ae442ac97df8bd503aac8336501dfbd120bdf9aba29c3487fc9'}
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'music.163.com',
                'Referer': 'http://music.163.com/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/66.0.3359.181 Safari/537.36'}
    data = {'params': params, 'encSecKey': encSecKey}
    try:    
        r=requests.post(url,data=data,headers=headers)
        result=json.loads(r.text)
        records=result['allData'][:10]
        songs=[i['song']['name'] for i in records]
        songs='^'.join(songs)
        artists=[i['song']['ar'][0]['name'] for i in records]
        artists='^'.join(artists)
        print(songs)
        print (artists)
        return(songs,artists)
    except:
        #print('error')
        return 0

#getRecords(1738459740)