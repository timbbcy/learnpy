#!python
# encoding:utf-8

import os
import requests
import re
from bs4 import BeautifulSoup
import time
import random

lst=list() 
rooturl=''
save_path_root='/home/python/zzh/'

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
"Host": "www.runoob.com",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Cookie":"SERVERID=0b225ae21c92e494e2a70e35b9a13daa|1522221898|1522206801; Hm_lvt_8e2a116daf0104a78d601f40a45c75b4=1520832945,1521541750,1522206777; Hm_lpvt_8e2a116daf0104a78d601f40a45c75b4=1522224188",
}

print("开始处理主页面 {}......".format(rooturl))
############请求获取网页内容##########################
content_rooturl = requests.get(rooturl, timeout=60,headers=headers).content    
############网页respose转BeautifulSoup################
soup = BeautifulSoup(content_rooturl, "html.parser", from_encoding='utf-8')    
urls_tmp = soup.find_all("a", class_="item-top item-1")

for item in urls_tmp:                                                    ########遍历soup.find_all结果
    ops=re.match(r'.+www.runoob.com/(.+)/.+html">',str(item)).group(1)   ########从网址中匹配出title,作为目录名

    if ops in lst:                                                       #######查重
        continue                                                         #######查重
    lst.append(ops)                                                      #######查重

    print("开始处理{}页面......".format(ops))
    dirname="{}{}/".format(save_path_root,ops)

    if os.path.exists(dirname) is False:                                 ###检查dirname是否存在，若没有，建目录
        os.makedirs(dirname)
        print("目录不存在mkdir {}".format(dirname))

    ############请求获取网页内容##########################
    content_second_url = requests.get("http:{}".format(item.get("href")), timeout=60,headers=headers).content
    ############网页respose转BeautifulSoup################
    soup_second_url = BeautifulSoup(content_second_url, "html.parser", from_encoding='utf-8')
    urls_tmp1=soup_second_url.find_all("a",target="_top")

    for item1 in urls_tmp1:                                               ########遍历soup.find_all结果
        ops1=item1.get_text().replace(' ','-').strip().replace('/','')    ########从网址中匹配出title,作为文件名
        print("开始处理{}页面......".format(ops1))
        filename="{}{}.html".format(dirname,ops1)

        if os.path.exists(filename):                                      ########检查filename是否存在,若已存在，跳出
            print("{}已处理过，continue......".format(filename))
            continue

        url_short=item1.get("href")                                          
        ########################匹配末端地址#######################
        if not re.match(r'^/',url_short) and not re.match(r'^http',url_short):
            url_short="http://www.runoob.com/{}/{}".format(ops,item1.get("href"))
        elif re.match(r'^http',url_short):
            url_short=item1.get("href")
        else:
            url_short="http://www.runoob.com{}".format(item1.get("href"))
        ###########################################################

        #############请求获取网页内容##############################
        content_third_url = requests.get(url_short,timeout=60,headers=headers).content
        #############网页respose转BeautifulSoup####################
        soup_third_url = BeautifulSoup(content_third_url, "html.parser", from_encoding='utf-8')
        last_content=soup_third_url.find_all("div",class_="article-intro")

        for element in last_content:                                      ########遍历soup.find_all结果
            with open(filename, 'w') as f:                                ########写文件
                f.write(str(element))
            time.sleep(random.randint(1,3))                               ########随机等待1到3秒

print("已完成爬取{}......".format(rooturl))
        

