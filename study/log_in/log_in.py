import requests
url =  "https://jaccount.sjtu.edu.cn/jaccount/ulogin"
        
headers = {"Referer":"https://jaccount.sjtu.edu.cn/jaccount/jal\
                    ogin?sid=jaoauth220160718&client=CMIMg6Qs4Ma4I\
                    pjmEcSlWd2wwzS7CP6a%2FRYkUyEOd0YF&returl=COrMmc%2BEA6U35\
                    XcgvNzqUkX0f%2FP0qTd0XVMCcjAztucfcS26G%2B2%2B7pZDFVwKdKxrKW\
                    ybUfbojRPDQoYz0DlDDGB2CcpeyPSN%2BJRo1Nhzsi7UVW%2FYYsV7AdPMmEjYK%2BjCTbev\
                    w%2FEAV7KHHwi%2BjXJxmrUClOeE6sJyOpJDZFnsoR1Qjyr34vdwUbWJ%2FDvsspqt962Az8gh8s7x%2\
                    FDwem3MMW0y9aBmC8j2uRrZOJ%2F76EDtYP5vYd2NOPXm3CjWcaoTHWS4lBUE1fEwyg7ORQKEQ4\
                    tUmIdxWVoGnvj%2BCIlJacoXmMjds80Xyp3UpBxDeKLKZpZ8wl7L05cbUhN60yR3ghZdKS0\
                    b8IwPC2OdPZkMkTUsqDu0lVkm%2F%2Br%2BWNNO8PHq14iTUpl6HZyxRoN7TKcTdXUIjc2o8ke0\
                    X7QkE22wt8i9Shrd90y3mDabXeYGc%2BWpLvtPyRyKC8PHOQ%2BCahiFY8H0%3D&se=CH%2F1mUg4v\
                    pSAKaBbFlByP%2FBjVFCT7r5p7ru46pxLCSCB%2F4Pd3uM4s55MYmcr15i1cw%3D%3D&v=&err=1",\
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",\
            "Origin": "https://jaccount.sjtu.edu.cn"
    
}

data ={ "sid":"jaoauth220160718",\
        "returl":"COrMmc+EA6U35XcgvNzqUkX0f/P0qTd0XVMCcjAztucfcS26G+2\
            +7pZDFVwKdKxrKWybUfbojRPDQoYz0DlDDGB2CcpeyPSN+JRo1Nhzsi7UVW\
            /YYsV7AdPMmEjYK+jCTbevw/EAV7KHHwi+jXJxmrUClOeE6sJyOpJDZFnsoR1\
            Qjyr34vdwUbWJ/Dvsspqt962Az8gh8s7x/Dwem3MMW0y9aBmC8j2uRrZOJ/76ED\
            tYP5vYd2NOPXm3CjWcaoTHWS4lBUE1fEwyg7ORQKEQ4tUmIdxWVoGnvj+CIlJacoXmMj\
            ds80Xyp3UpBxDeKLKZpZ8wl7L05cbUhN60yR3ghZdKS0b8IwPC2OdPZkMkTUsqDu\
            0lVkm/+r+WNNO8PHq14iTUpl6HZyxRoN7TKcTdXUIjc2o8ke0X7QkE22wt8\
            i9Shrd90y3mDabXeYGc+WpLvtPyRyKC8PHOQ+CahiFY8H0=",\
        "se":"CH/1mUg4vpSAKaBbFlByP/BjVFCT7r5p7ru46pxLCSCB/4Pd3uM4s55MYmcr15i1cw==",\
        "v":"",\
        "uuid":"47cb17fd-5aba-44c8-bc23-0295b995e7db",\
        "client":"CMIMg6Qs4Ma4IpjmEcSlWd2wwzS7CP6a/RYkUyEOd0YF",\
        "user":"elftat",\
        "pass":"201123Down",\
        "captcha":"aanck",\
        "g-recaptcha-response":"03AHaCkAaLfj0rROdPxxuB\
                                uSofU3rXZfrr2cuVgT3q9Ii7lqxG6jaH8h1v5m4dBgPRX2odbzngf_3Dk\
                                EH1atmSWWqI4CjyH9UkNI2sITne1O-buF6YXiP-IOjf3-i5kAogoSO-xaXGj4-hh\
                                D0Jg3Hzg2p0QFqS8A3n2tFG_N1pjdSRab80bf0j1D7F2FMbD0jKn3QD9wguXOoXTcZNha\
                                _-GyL7pY0PtWIjEWGMih-IcEJlaNvpxbDUnDfaMK_5C3P5lSB7BiOB8JaGa5rmhQGTpCbAW\
                                YjcidZ2hWErppAkn3nO5JOLeFKVRmVWe5XKUmxTuxRiR0Zme8NA2IBSKO1Y379JJI-hUwXGmr\
                                BPOr2PU_eGTRiFhBEgrEnh3QUm3Q33OAU5u5jzPgYMWOm5Lv0E597QB51RY0WQog"
        }
r = requests.post(url,headers = headers,timeout=30,data = data)
r.raise_for_status()
with open("./study/log_in/log_in.html","wb") as f:
    f.write(r.content)