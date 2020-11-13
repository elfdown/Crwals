#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

try:
    ip_n="111.45.3.77"
    kv = {"user-agent":"Mozolla5.0"}
    qu = {"ip":ip_n}
    r = requests.get("http://m.ip138.com/ip.asp",params = qu,timeout=30,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
    print(r.text[1900:-250])
except:
    print("请求异常")