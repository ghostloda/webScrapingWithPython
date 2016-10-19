from bs4 import BeautifulSoup
import requests
import urllib
import time
'''
抓取多个页面的图片
首先分析 每个页面的url
http://www.meizitu.com/a/5464.html
http://www.meizitu.com/a/5463.html
http://www.meizitu.com/a/5462.html
....
根据不同点  试着抓取5张页面，也就是5450到5454，
'''
#构造url
urls = ['http://www.meizitu.com/a/{0}.html'.format(str(i)) for i in range(5450,5455)]
#爬取
i=0
for url in urls:
    i+=1
    wb_data = requests.get(url)
    time.sleep(3)
    wb_data.encoding='GBK'  #字符串本身，是某种编码的，但是输出，显示，到终端时，终端所使用编码，和你字符串的编码不一样，导致无法正常显示。
                             #比较常见的是，本身是UTF-8类型的字符串，但是却将其输出到Windows的cmd中，而cmd中默认是GBK编码的，
                            # 导致两者不匹配，所以打印字符串时，出现乱码
                             #http://www.crifan.com/summary_python_2_x_common_string_encode_decode_error_reason_and_solution/
    soup = BeautifulSoup(wb_data.text,'html.parser')
    img = soup.select('#picture > p > img')
    url_data = []
    for m in img:
        ima_url=m.get('src')
        url_data.append(ima_url)

    #下载图片到本地
    j=0
    for url_img in url_data:
         f=open('G:\妹子图\%d%d.jpg'%(i,j),'wb')
         req=urllib.request.urlopen(url_img)
         buf=req.read()
         f.write(buf)
         j+=1