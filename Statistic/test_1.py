# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 16:38
# @Author  : ZHAO Jinbo
# @File    : test.py
# @Software: PyCharm
with open('hello.txt','r') as f:
    p1=f.readline()
    print(f.tell())
    p2=f.read()+"P2"
    print(f.tell())
print(p1)
print(p2)