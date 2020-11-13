import requests
from bs4 import BeautifulSoup

url = "https://h.bilibili.com/1019234?from=search&seid=4037731788968455319"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
li = []
for i in soup.find_all(True):
    li.append(i.name)
s = set(li)
li = list(s)
print(li)