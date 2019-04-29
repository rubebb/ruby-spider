#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest,time,re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

class GoogleUrlSearch(unittest.TestCase):

    list = []
    word = ''

    def setUp(self):
        self.word = raw_input(u'Tell me what u want to search:').decode('utf-8')
        #用你的搜狐
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        #搜索
        list = self.list
        driver = self.driver
        driver.get("https://www.google.com/search?tbm=nws&q={q}".format(q=self.word))
        assert "Google" in driver.title
        for i in range(2,12):
            # 怕跳太快了 给了sleep
            time.sleep(1.33)
            #拿源码分析
            page = driver.page_source
            self.checkURL(page)
            #换页
            elem = driver.find_element_by_link_text(str(i))
            elem.click()
        self.printList(list)

    def checkURL(self,html):
        soup = bs(html, 'html.parser')
        pp = soup.find_all('div',attrs={'class':'gG0TJc'})
        for i in pp:
            try:
                www=re.findall('href="(.*?)" onmousedown',str(i))[0]
                title = re.findall('event\)">(.*?)</a',str(i))[0].replace('<em>','').replace('</em>','')
                time = re.findall('fwzPFf">(.*?)</span',str(i))[0]
                # print time +' '+ www +''+title
                self.list.append(title +'--'+ www +'--'+time)
            except:
                pass

    def printList(self,list):
        for i in range(len(list)):
            try:
                print list[i]
            except:
                pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()