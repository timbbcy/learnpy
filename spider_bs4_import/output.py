

#!python
# encoding:utf-8
import time

class Output:
    def output(content,filename):
        for element in content:                                      ########遍历soup.find_all结果
            with open(filename, 'w') as f:                                ########写文件
                f.write(str(element))
            time.sleep(1)
