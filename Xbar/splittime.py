# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 15:06
# @Author  : ZHAO Jinbo
# @File    : splittime.py
# @Software: PyCharm
import xlrd
import time, datetime


def excel_time(cell_value):
    year, month, day, hour, minute, second = xlrd.xldate_as_tuple(cell_value, book.datemode)
    time_date = datetime.datetime(year, month, day, hour, minute, second)
    return time_date


book = xlrd.open_workbook("database.xlsx")
sh = book.sheet_by_index(0)  # 按照顺序获得第一个sheet
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))

sub_num = 5
dict_value = {}
# 获得第一组数据
time_start = excel_time(sh.cell_value(0, 3))

for rx in range(sh.nrows):
    time_current = excel_time(sh.cell_value(rx, 3))
    time_diff = (time_current - time_start).total_seconds()
    if time_diff > 1800:
        value_list = []
        try:
            for j in range(sub_num):
                value_list.append(sh.cell_value(rx + sub_num, 7))
            dict_value[time_current.strftime("%m/%d/%Y %I:%M:%S %p")] = value_list
            time_start = time_current
        except:
            break

print(dict_value)
print(len(dict_value))
