# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
url = 'http://www.meizitu.com/a/5450.html'
wb_data = requests.get(url)
wb_data.encoding='GBK'  #字符串本身，是某种编码的，但是输出，显示，到终端时，终端所使用编码，和你字符串的编码不一样，导致无法正常显示。
                         #比较常见的是，本身是UTF-8类型的字符串，但是却将其输出到Windows的cmd中，而cmd中默认是GBK编码的，导致两者不匹配，所以打印字符串时，出现乱码
                         #http://www.crifan.com/summary_python_2_x_common_string_encode_decode_error_reason_and_solution/
soup = BeautifulSoup(wb_data.text,'html.parser')
img = soup.select('#picture > p > img')
url_data = []
for i in img:
    ima_url=i.get('src')
    url_data.append(ima_url)

#下载图片到本地
i=0
for url in url_data:
     f=open('G:\妹子图\%d.jpg'%i,'wb')
     req=urllib.request.urlopen(url)
     buf=req.read()
     f.write(buf)
     i+=1
