#-*- coding: UTF-8 -*-

import requests,urllib
from bs4 import BeautifulSoup as bs
import re

def urlfromYahoo(word):
    list = []
    for i in range(0,10):
        page = i * 10 + 1
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87'}
        url ='https://hk.search.yahoo.com/search?fr=yfp-search-sb&p={name}&b={page}'.format(name=urllib.quote(word),page=page)
        html = requests.get(url=url,headers=headers,timeout=5)
        html.encoding = 'gbk'  # 将编码格式设置为utf-8
        soup = bs(html.content, 'lxml', from_encoding='utf-8')
        pp = soup.find_all('a',attrs={'href':re.compile('^http'),'target':'_blank','referrerpolicy':'origin','class':'ac-algo fz-l lh-20 tc d-ib va-mid'})
        for i in pp:
            try:
                www = re.findall('href="(.*?)"',str(i))[0]
                title = (re.findall('target="_blank">(.*?)</a>',str(i))[0]).replace('<b>','').replace('</b>','')
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
