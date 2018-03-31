#!python
# encoding:utf-8
#
import re
import os
import download,match_judge,output

rooturl='http://www.runoob.com'

def run(url):
    save_path_root='/home/python/zzh/runoob/'
    lst=list()
    print("开始处理主页面 {}......".format(rooturl))
    soup = download.Download.download(rooturl)
    urls_tmp = soup.find_all("a", class_="item-top item-1")
    for item in urls_tmp:                                                    ########遍历soup.find_all结果
        ops=re.match(r'.+www.runoob.com/(.+)/.+html">',str(item)).group(1)   ########从网址中匹配出title,作为目录名
        if ops in lst:                                                       #######查重
            continue                                                         #######查重
        lst.append(ops)                                                      #######查重
        dirname="{}{}/".format(save_path_root,ops)
        match_judge.MatchAndJudge.judge_mkdir_dir(dirname)
        print("开始处理{}页面......".format(ops))
        soup_second_url = download.Download.download("http:{}".format(item.get("href")))
        urls_tmp1=soup_second_url.find_all("a",target="_top")
        for item1 in urls_tmp1:                                               ########遍历soup.find_all结果
            ops1=item1.get_text().replace(' ','-').strip().replace('/','')    ########从网址中匹配出title,作为文件名
            filename="{}{}.html".format(dirname,ops1)
            if os.path.exists(filename):                                      ########检查filename是否存在,若已存在，跳出
                print("{}已处理过，continue......".format(filename))
                continue
            print("开始处理{}页面......".format(ops1))
            url_short=match_last_url(item1.get("href"))
            soup_third_url = download.Download.download(url_short)
            last_content=soup_third_url.find_all("div",class_="article-intro")
            output.Output.output(last_content,filename)                                     ########随机等待1到3秒
    print("已完成爬取{}......".format(rooturl))

if __name__ == '__main__':
    run(rooturl)