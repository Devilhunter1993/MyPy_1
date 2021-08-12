# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 19:59
# @Author  : ZHAO Jinbo
# @File    : mysql_test.py
# @Software: PyCharm

import pymysql
import xlrd

# 设置连接信息
host = 'localhost'
port = 3306
db = 'test_db'
user = 'root'
password = 'zjb123'
# 获得连接
conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
# 获得游标对象
cursor = conn.cursor(pymysql.cursors.DictCursor)

book = xlrd.open_workbook("test.xls")
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)  # 按照顺序获得第一个sheet
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# 获得所有需要插入的数据
for rx in range(sh.nrows):
    insert_data = sh.cell_value(rx, 0).strip()
    try:
    # 创建sql语句
        sql = "insert into excel_t(name) values(%s)"
    # 执行语句
        cursor.execute(sql,insert_data)
    # 事物提交
        conn.commit()
    except:
        print('插入异常')
# 关闭数据库连接
cursor.close()
conn.close()
