# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url= "http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST"
#为了应付防爬机制，构造手机端浏览headers
headers = {
    'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

web_data = requests.get(url,headers=headers)
soup = BeautifulSoup(web_data.text,"lxml")

images = soup.select('div.thumb.thumbLLR.soThumb > img')
for img in images:
    print img.get('src')




#多页爬虫的urls构造 urls=["http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST.format(str(i)) for i in range(30,930,30)]