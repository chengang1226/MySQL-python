#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Time : 2019/5/29 20:24
# @Author : 陈港
# @File : MySQL-python的介绍.py
# @Software : PyCharm

# python操作mysql的几种方式

# MySQL-python 又叫 MySQLdb，是 Python 连接 MySQL 最流行的一个驱动，很多框架都也是基于此库进行开发，
# 遗憾的是它只支持 Python2.x，而且安装的时候有很多前置条件，因为它是基于C开发的库，在 Windows 平台安装非常不友好，
# 经常出现失败的情况，现在基本不推荐使用，取代的是它的衍生版本。
# 下载地址：https://pypi.org/project/MySQL-python/#files

# 由于 MySQL-python 年久失修，后来出现了它的 Fork 版本 mysqlclient，完全兼容 MySQLdb，同时支持 Python3.x，
# 是 Django ORM的依赖工具，如果你想使用原生 SQL 来操作数据库，那么推荐此驱动。
# Windows 可以在https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient 网站找到 对应版本的 whl 包下载安装。

# PyMySQL 是纯 Python 实现的驱动，速度上比不上 MySQLdb，但它的安装方式没那么繁琐，同时也兼容 MySQL-python。

# peewee 写原生 SQL 的过程非常繁琐，代码重复，没有面向对象思维，继而诞生了很多封装 wrapper 包和 ORM 框架，
# ORM 是 Python 对象与数据库关系表的一种映射关系，有了 ORM 你不再需要写 SQL 语句。提高了写代码的速度，同时兼容多种
# 数据库系统，如sqlite, mysql、postgresql，付出的代价可能就是性能上的一些损失。如果你对 Django 自带的 ORM 熟悉的话，
# 那么 peewee的学习成本几乎为零，它是 Python 中是最流行的 ORM 框架。

# SQLAlchemy是一种既支持原生 SQL ，又支持 ORM 的工具，它非常接近 Java 中的 Hibernate 框架。

# 导入MySQLdb包
import MySQLdb

# 连接数据库
conn = MySQLdb.connect(
             host="localhost",                  # host:数据库主机名,默认是用本地主机
             user="root",                       # user:数据库登陆用户名,默认是当前用户
             passwd="125179chengang",           # passwd:数据库登陆的密码
             db="mysql",                        # db:要使用的数据库名
             port=3306,                         # port:MySQL服务使用的TCP端口,默认是3306
             charset="utf8"                     # charset:数据库编码
             )

# 使用cursor()方法获取操作游标
cur = conn.cursor()

# 创建数据库表
sql_1 = """CREATE TABLE Product (
         product_id CHAR(4) NOT NULL,
         product_name VARCHAR(100) NOT NULL,
         product_type VARCHAR(32) NOT NULL,
         sale_price INT ,
         purchase_price INT )"""
cur.execute(sql_1)
conn.commit()
conn.close()

# 向表格批量插入数据
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_2 = 'insert into Product(product_id, product_name, product_type, sale_price, purchase_price) ' \
        'values (%s, %s, %s, %s, %s)'
param = (('0001', '休闲裤', '服装', 1000, 500), ('0002', '打孔器', '办公用品', 500, 320),
         ('0003', '针织衫', '服装', 4000, 2000), ('0004', '电饭锅', '厨房用品', 3000, 1500),
         ('0005', '纯牛奶', '饮品', 2000, 1200), ('0006', '电脑', '办公用品', 10000, 5200),
         ('0007', '书本', '图书', 1500, 600), ('0008', '洗衣液', '生活用品', 1200, 400))
cur.executemany(sql_2, param)
conn.commit()
cur.close()

# 增加数据
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_3 = 'insert into Product(product_id, product_name, product_type, sale_price, purchase_price) ' \
        'values ("0009", "雨伞", "生活用品", 2200, 1000)'
cur.execute(sql_3)
conn.commit()

# 删除数据
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_4 = 'delete from Product where product_id = "0007"'
cur.execute(sql_4)
conn.commit()

sql_5 = 'delete from Product where sale_price >%s ' % ("4000")
try:
    cur.execute(sql_5)
    conn.commit()
except:
    conn.rollback()
conn.close()

# 数据查询
# 条件查询（通过where语句设定条件）
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_6 = "select * from Product where purchase_price > %s" % (1200)
try:
    cur.execute(sql_6)
    result1 = cur.fetchall()
    for row in result1:
       product_id = row[0]
       product_name = row[1]
       product_type= row[2]
       sale_price = row[3]
       purchase_price = row[4]
       print("product_id=%s, product_name=%s, product_type=%s, sale_price=%s, purchase_price=%s" % \
              (product_id, product_name, product_type, sale_price, purchase_price))
except:
    print("Error: unable to fetch data")

# 投影查询（返回指定列的数据）
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_7 = "select product_id, purchase_price from Product"
try:
    cur.execute(sql_7)
    result2 = cur.fetchall()
    for row in result2:
        print("product_id=%s, purchase_price=%s" % row)
except:
    print("Error: unable to fetch data")

# 排序查询
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_8 = "select product_id, sale_price from Product order by sale_price desc"
try:
    cur.execute(sql_8)
    result3 = cur.fetchall()
    for row in result3:
        print("product_id=%s, sale_price=%s" % row)
except:
    print("Error: unable to fetch data")

# 聚合查询（对表格数据进行简单处理）
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_9 = "select count(*) from Product"
try:
    cur.execute(sql_9)
    result_4 = cur.fetchall()
    print(result_4)
except:
    print("Error: unable to fetch data")

sql_10 = "select avg(sale_price) from Product"
cur.execute("select avg(sale_price) from Product")
try:
    cur.execute(sql_10)
    result_5 = cur.fetchall()
    print(result_5)
except:
    print("Error: unable to fetch data")

# 数据更新
import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="125179chengang", db="mysql", charset="utf8")
cur = conn.cursor()
sql_11 = 'update Product set sale_price = 3000 where product_id = "0003"'
try:
    cur.execute(sql_11)
    conn.commit()
except:
    conn.rollback()



