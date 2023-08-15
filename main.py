# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import json
num = 1
for i in range(68):
    urls = f"https://weciimaa.online/download-series/?page_number={num}/"

    response = requests.get(urls).text

    supe = BeautifulSoup(response, "lxml")
    data = {}
    for filme in supe.find("div",{"class":"Grid--WecimaPosts"}).find_all("div", {"class": 'GridItem'}):
        name = filme.find("strong",{"class":"hasyear"}).text
        url = filme.find("a")["href"]
        data[str(name)].append(str(url))
    num+=1

with open("file_list.json","w", encoding='utf-8') as f:
        json.dump(data, f)

