# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
'''\
爬取纽约市的热门景点名称 图片 标签 评论数量
'''
url= "http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST"
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
# }
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,'lxml')
images = soup.select('img[width="160"]')
titles = soup.select('div.property_title > a[target="_blank"]')
cates = soup.select('div.p13n_reasoning_v2')
comments =soup.select('div.wrap > div.rs.rating > span.more > a[target="_blank"]')

for img, title ,cate,comment in zip(images,titles,cates,comments):
    data = {
        'img':img.get('src'),
        'title': title.get_text(),
        'cate': list(cate.stripped_strings),
        'comment':comment.get_text(),
    }
    print repr(data).decode("unicode–escape")   #print data 控制台显示的是unicode字符，不方便观察，而不是中文,这里用repr(data).decode("unicode–escape")做一下转换
