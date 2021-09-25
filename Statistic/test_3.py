# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 20:36
# @Author  : ZHAO Jinbo
# @File    : test_3.py
# @Software: PyCharm
lst=[(8, ['143', '224', '134']), (9, ['342', '252']), (13, ['562']), (15, ['267', '276'])]
result = list(map(sorted, [x[1] for x in lst] ))
print(result)


import numpy as np
nArry=np.ones((3,4))
print(nArry)
print(type(nArry[0]))