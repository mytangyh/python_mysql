#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
测试封装
"""
from pymysql_comm import UsingMysql


def check_it():
    with UsingMysql(log_time=True) as um:
        um.cursor.execute("select count(id) as total from Product")
        data = um.cursor.fetchone()
        print("-- 当前数量: %d " % data['total'])


if __name__ == '__main__':
    check_it()
