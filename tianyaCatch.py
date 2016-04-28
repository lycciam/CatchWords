# 抓取天涯论坛的“某些”相关信息
import requests
import os
from bs4 import BeautifulSoup
import xlsxwriter
import time

url = 'http://search.tianya.cn/bbs?q=%E6%95%99%E5%B8%88%E7%BD%A2%E8%AF%BE&pn='


def getSoup(url):
    page = requests.get(url)
    Soup = BeautifulSoup(page.text, 'lxml')
    return Soup


def getData(soup, info):
    for item in soup:
        if item.find('p', 'source'):
            data = {
                'title': item.select('h3 > a')[0].get_text(),
                'url': item.select('h3 > a')[0].get('href'),
            }
        else:
            None
        info.append(data)
        print(data)


info = []
for i in range(75):
    url_t = url + str(i)
    soup = getSoup(url_t)
    time.sleep(2.5)
    Soup_target = soup.select('div.searchListOne > ul > li')
    getData(Soup_target, info)

print(info)
