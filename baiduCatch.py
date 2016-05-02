import requests
from bs4 import BeautifulSoup
import json
from docx import Document

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 '
                  'Safari/537.36'
}

url = 'http://tieba.baidu.com/p/3618228828'

page = requests.get(url, header)
soup = BeautifulSoup(page.text, 'lxml')

# print(soup.prettify())

'''
    所在吧，作者，发帖时间，post_id，
'''

init = soup.select('div.p_postlist > div')[0]
print(init)

time = init.get('data-field', 'N/A')
time = json.loads(time)
# print('title:', soup.select('title')[0].get_text())
# print('time:', time['content']['date'])
# print('author:', time['author']['user_name'])
# print('post_id:', time['content']['post_id'])
# print('回复数量:',
#       soup.select('#thread_theme_5 > div.l_thread_info > ul > li:nth-of-type(2) > span:nth-of-type(1)')[0].get_text())
# print('总页数:',
#       soup.select('#thread_theme_5 > div.l_thread_info > ul > li:nth-of-type(2) > span:nth-of-type(2)')[0].get_text())

# 初始化文档
document = Document()

# 获取基本信息
document.add_paragraph('url:' + url)
document.add_paragraph("title:" + soup.select('title')[0].get_text())
document.add_paragraph("time:" + time['content']['date'])
document.add_paragraph("author:" + time['author']['user_name'])
document.add_paragraph('post_id:' + time['content']['post_id'])
document.add_paragraph('回复数量:' + soup.select('#thread_theme_5 > div.l_thread_info > ul > li:nth-of-type(2) > '
                                             'span:nth-''of-type(1)')[0].get_text())
document.add_paragraph('总页数:' + soup.select('#thread_theme_5 > div.l_thread_info > ul > li:nth-of-type(2) > span:nth-'
                                            'of-type(2)')[0].get_text())

# 获取一楼信息
# 作者，发布时间，子贴id，回复数量，帖子内容
document.add_paragraph("")
document.add_paragraph("author:" + time['author']['user_name'])
