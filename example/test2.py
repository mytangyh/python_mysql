#! /usr/bin/python
# -*- coding: UTF-8 -*-


from pymysql_lib_1 import UsingMysql


def check_it():

    with UsingMysql(log_time=True) as um:
        sql = "select count(id) as total from Product"
        print("-- 当前数量: %d " % um.get_count(sql, None, 'total'))

if __name__ == '__main__':
    check_it()