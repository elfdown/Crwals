#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def get_http_text(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return(r.text)
    except:
        return("请求异常")

if __name__ == "__main__":
    url="https://dev.bbs.sjtu.edu.cn/c/10-category/26-category"
    print(get_http_text(url))
        
