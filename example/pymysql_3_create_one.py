#! /usr/bin/python
# -*- coding: UTF-8 -*-

from pymysql_comm import UsingMysql


def select_one(cursor):
    cursor.execute("select * from Product")
    data = cursor.fetchone()
    print("-- 单条记录: {0} ".format(data))


# 新增单条记录
def create_one():

    with UsingMysql(log_time=True) as um:
        sql = "insert into Product(name, remark) values(%s, %s)"
        params = ('男士双肩背包1', '这个是非常好的背包')
        um.cursor.execute(sql, params)

        # 查看结果
        select_one(um.cursor)

if __name__ == '__main__':
    create_one()

