# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
urls = ['http://nj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,11)] #构造十页url
def get_xiaozhu(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    time.sleep(2)
    images = soup.select('ul > li > a > img')
    prices = soup.select('span.result_price > i')
    titles = soup.select('div.result_intro > a > span')
    owner_images =soup.select('span.result_img > a > img')
    print images
    for img,price,title,owner_img in zip(images,prices,titles,owner_images):
        data = {
            'img':img.get('lazy_src'),
            'price':price.get_text(),
            'title':title.get_text(),
            'owner_img':owner_img.get('lazy_src')
        }
        print repr(data).decode("unicode–escape")


for url in urls:
    get_xiaozhu(url)