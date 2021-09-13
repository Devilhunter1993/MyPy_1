# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 16:38
# @Author  : ZHAO Jinbo
# @File    : test.py
# @Software: PyCharm
import math


def primeNum(num: int) -> bool:
    if num == 1:
        return False
    elif num == 2:
        return True
    k = math.sqrt(num)
    i = 2
    while i <= k:
        if num % i == 0: return False
        i += 1
    if i > k:
        return True


count = 0
i = 2
while count != 6:
    M = 2 ** i - 1
    if primeNum(i) and primeNum(M):
        count += 1
        print(count, i, M)
    i += 1
