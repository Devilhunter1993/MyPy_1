# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 16:38
# @Author  : ZHAO Jinbo
# @File    : test.py
# @Software: PyCharm
import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常#
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))

import requests

res = requests.get("https://www.csdn.net/eee",  timeout=1)
res.encoding = "utf8"
res.raise_for_status()
print(res.status_code)
print(res.text)
