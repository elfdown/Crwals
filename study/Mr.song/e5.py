#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
kv = {"user-agent":"Mozolla5.0"}
r = requests.get("https://www.bilibili.com/",timeout=30,headers = kv)
r.encoding = r.apparent_encoding
help(r)
