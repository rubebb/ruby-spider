#-*- coding: UTF-8 -*-

import requests,urllib
from bs4 import BeautifulSoup as bs
import re

def urlfromYahoo(word):
    list = []
    len1 = 0
    for i in range(0,10):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'}
        url = "https://cn.bing.com/search?q={word}&qs=n&sp=-1&pq=tian%27x&sc=8-6&sk=&ensearch=1&first={page}&FORM=PERE".format(word=urllib.quote(word), page=i*10)
        html = requests.get(url=url, headers=headers, timeout=5)
        html.encoding = 'gbk' 
        soup = bs(html.content, 'lxml', from_encoding='utf-8')
        pp = soup.find_all('h2')
        if(i==0):
            len1 = int(len(pp) -4)
        else:
            len1 = len(pp)
        for i in range(len1):
            try:
                www=re.findall('href="(.*?)"', str(pp[i]))[0]
                title=re.findall('">(.*?)</a',str(pp[i]))[0].replace('<strong>','').replace('</strong>','')
                # print(title)
                list.append(www+''+title)
            except:
                pass
    return list

if __name__ == '__main__':
    list = urlfromYahoo(raw_input(u'Tell me what u want to search:'))
    for i in range(len(list)):
        try:
            print list[i]
        except:
            pass
