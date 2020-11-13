#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def get_http_text(url):
    try:
        kv = {"user-agent":"Mozolla5.0"}
        r = requests.get(url,timeout=30,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return(r.text)
    except:
        return("请求异常")

if __name__ == "__main__":
    url="http://www.cs.hit.edu.cn/11447/list.htm"
    print(get_http_text(url))