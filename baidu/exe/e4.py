import requests
from lxml import etree

url = "http://icanhazip.com"
if __name__ == "__main__":
    try:
        r = requests.get(url)
        r.raise_for_status()
        tree = etree.HTML(r.text)
        print(tree)
        ip = tree.xpath("//pre/text()")
        print("the ip address is {}".format(ip))
    except:
        print("something is wrong")
    