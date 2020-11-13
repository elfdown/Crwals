import json
import requests
import time
import numpy as np
import pandas as pd

url = "http://www.sczwfw.gov.cn/app/search/duplicateNnameQuery"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/80.0.3987.163 Safari/537.36',
    'Referer': 'https://music.163.com/http://www.sczwfw.gov.\
                cn/app//search/neonatal?areaId=1431&areaCode=510000000000',
    'Origin':'http://www.sczwfw.gov.cn'
}

def get_count(name,url,headers):
    data = {
        "appid":"5000",
        "name":"{}".format(name),
        "location":"/app",
        "businessType":"2500"
    }
    r = requests.put(url=url,data=data,headers=headers)
    r.raise_for_status()
    jdata = json.loads(r.content)
    print(jdata)
    count = jdata["data"][0]["COUNT"]
    return(count)


def json_print(dic):
    string = json.dumps(dic,ensure_ascii = False, indent = 4)
    print(string)

if __name__ == "__main__":
    with open("resualt.json","r") as f:
        name_dict = json.load(f)
    xlsx = pd.ExcelFile("name.xlsx")
    for sheet_name in xlsx.sheet_names:
        df = pd.read_excel(xlsx,sheet_name)
        i = 11
        for name_str in df["姓名"][(i-1)*5:i*5]:
            time.sleep(10)
            name = name_str.strip('\n')
            count = get_count(name,url=url,headers=headers)
            name_dict[name] = count

    with open("resualt.json","w") as f:
        json.dump(name_dict,fp=f,ensure_ascii = False, indent = 4)
