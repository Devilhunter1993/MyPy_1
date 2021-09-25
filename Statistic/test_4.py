# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 10:03
# @Author  : ZHAO Jinbo
# @File    : test_4.py
# @Software: PyCharm
import numpy as np
"""
aArry=np.array([(1,2,3),(4,5,6)])
print(aArry[:,[0,1]])
print(aArry[:,[0,1]])

bArry=np.array([[1,2,3],[4,5,6],[7,8,9]])


b = np.arange(24).reshape(2, 3, 4)
print(b)
c=b[:, 0, 0]

print(c)


a=np.random.rand(3,5)
b=np.arange(a.shape[0])
mask=np.random.choice(np.arange(a.shape[0]),2,replace=True)

a=np.arange(10,21)
print(type(a<15))

print(a[a<15])


socre=np.array([[98,76,87],[76,88,91]])
print(socre)
socre_mean=socre.mean(axis=1,keepdims=True)
print(socre_mean)

import numpy as np
import time
import math
aArray=np.arange(10000001)

t1=time.process_time()
np.sin(aArray)
t2=time.process_time()
print("Numpytime: ", t2 - t1)


t1=time.process_time()
for i in aArray:
    math.sin(i)
t2=time.process_time()
print("Math time: ", t2 - t1)


a=sorted(set('You need Python.'))[2]
b=sorted(set('You need Python.'))


dict_mark = {'Wang': 'C', 'Li': 'B', 'Ma': 'A'}
s = ''
for c in dict_mark.values():
    s += c

dict_mark_1 = {'Wang': 98, 'Li': 87, 'Ma': 93}
dict_mark_2 = {'Li': 90, 'Ma': 95, 'Xu': 75}
dict_mark_1.update(dict_mark_2)
dict_mark_1.pop('Li')
"""

from pandas import Series, DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print(frame)
print(type(frame["IDE"]))
print('VS' in frame['IDE'].values)


print(frame['year'][2])

