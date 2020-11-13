import requests

url = "https://music.163.com/song?id=1439975538"
headers = { "Host": "music.163.com",\
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",\
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",\
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",\
            "Accept-Encoding": "gzip, deflate, br",\
            "Connection": "keep-alive",\
            "Referer": "https://music.163.com/",\
            "Cookie": "_ntes_nnid=fbf587d796566bae535bf62ceaccfe08,1568698259421; _ntes_nuid=fbf587d796566bae535bf62ceaccfe08; JSESSIONID-WYYY=Zn%2BtlSxgWoCWJm54OlOf8v2ggMld4%2Bcg%5CNd8dCraBzoRs0bG%2Fdm8qTlzh79z%5CPjYyF76M%5Cxg%2F20dw9mSM0CMv3Zs8ueDJkdriHs1m5y2Bxt%5CRmvMVsu7hE%2B%2FiOh7H7TntcqvaA%5CsZY72y2onVAJ0%2FpzP0RcDRNTYsQUte527sQM9nymT%3A1586495832503; _iuqxldmzr_=32; WM_NI=thNSVRgCtHzEGYtd09OvqkDIm75I8vIg1V5ITE%2B38Ffj7XLp4oi3XBhoxqjVBgqP2aes%2BQcKjkbFrSxTnf8lFe1AqD%2But%2FARshlpWmPYO7Io0%2FPlCQ1J1sfALL%2F84BoXVU4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacc621aeedffb6b15081868ea2c85f969b9eabae4baab98d95f36aabbbe194b72af0fea7c3b92ab8b882b4d55aa59dbca9f94f8587bc85b3338daabf8cc743afe9fbaabb7e8bb9ffb7b843989be5d4bb4ea6b6f9b9cf7cf8b1a7d4db4aacb1b892e95e82b9bfb1b16ba7ade5b2e241aab5aea7f159bc8ca287bb6886bbffa2f450e9abbcd0c45ab1b8a491d667948781d8cc65f4f1a08dc25bf396ff94e54b9094e1d9b74aad889ab6b737e2a3; WM_TID=xv2bRIAI06hABBEBBFd9rH3JgmLhC85s; __oc_uuid=930be4a0-081f-11ea-8d7e-b3126048127a; usertrack=ezq0ZV3dBKAuAR2QAxs4Ag==; ntes_kaola_ad=1; MUSICIAN_COMPANY_LAST_ENTRY=483627976_musician; MUSIC_U=105f358edbb1f453eb29e2f2012742f03afc025b03fe6fca61c74018a5e1ea27d18ecdc65356b78abd3a3890c08ed134114f327788dd6fe3; __remember_me=true; __csrf=bc89e416ad2b04dd5ee170122b9c6371; playerid=68358201",\
            "Upgrade-Insecure-Requests": "1",\
            "TE": "Trailers"}

if __name__ == "__main__":
    r = requests.get(url,headers = headers,timeout = 30)
    r.raise_for_status()
    with open("test.html","wb") as f:
        f.write(r.content)
    