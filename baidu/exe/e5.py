import requests
# 待测试目标网页
targetUrl = "http://icanhazip.com"
def get_proxies():
    # 代理服务器


    for i in range(1,6):
        resp = requests.get(targetUrl, proxies=proxies)
        # print(resp.status_code)
        print('第{}次请求的IP为：{}'%(i,resp.text))
        
get_proxies()