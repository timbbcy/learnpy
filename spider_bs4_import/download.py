#!python
# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import random
import time

class Download:
    def download(url,headers):
        time.sleep(random.randint(1,2))
        content=requests.get(url,timeout=60,headers=headers).content
        soup = BeautifulSoup(content,"html.parser",from_encoding='utf-8')
        return soup
