import os
import re

class MatchAndJudge:
    ########################匹配末端地址#######################
    def match_last_url(url,rooturl):
        if not re.match(r'^/',url) and not re.match(r'^http',url):
            url="{}/{}/{}".format(rooturl,ops,item1.get("href"))
        elif re.match(r'^http',url):
            url=item1.get("href")
        else:
            url="{}{}".format(rooturl,item1.get("href"))

    ###检查dirname是否存在，若没有，建目录
    def judge_mkdir_dir(dirname):
        if os.path.exists(dirname) is False:
            os.makedirs(dirname)
            print("目录不存在mkdir {}".format(dirname))

    def match_rooturl(url):
        return re.match(r'http://(.+)',url).group(1)
