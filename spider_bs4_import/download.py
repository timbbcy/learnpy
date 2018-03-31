
#!python
# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import random
import time

class Download:
    def download(url):
        headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
        "Host": "www.runoob.com",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Cookie":"SERVERID=0b225ae21c92e494e2a70e35b9a13daa|1522221898|1522206801; Hm_lvt_8e2a116daf0104a78d601f40a45c75b4=1520832945,1521541750,1522206777; Hm_lpvt_8e2a116daf0104a78d601f40a45c75b4=1522224188",
        }
        time.sleep(random.randint(1,2))
        content=requests.get(url,timeout=60,headers=headers).content
        soup = BeautifulSoup(content,"html.parser",from_encoding='utf-8')
        return soup
