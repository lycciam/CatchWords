import requests
from bs4 import BeautifulSoup
import json
from docx import Document
import requests.packages.urllib3.util.ssl_
import logging.handlers
import time
import pandas
import baiduCatch

# 预防ssl问题发生；
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

# 声明日志区
# 日志的区域需要另外去写
log_file = 'F:\\work_of_spyder\\Logfile\\get.log'
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s - %(msecs)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('done')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    workfile = 'F:\\work_of_spyder\\'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 '
                      'Safari/537.36'}
    data = pandas.read_excel('f:\\B.xlsx')
    for url in data['url']:
        test = baiduCatch.isnone_tieba(url)
        if test == 1:
            baiduCatch.get_tiezi_info(url, header, workfile)
            logger.info('get url: ' + url)
        time.sleep(1)

