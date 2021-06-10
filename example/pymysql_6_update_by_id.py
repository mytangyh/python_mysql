#! /usr/bin/python
# -*- coding: UTF-8 -*-

from pymysql_comm import UsingMysql


def update_by_pk(cursor, name, pk):
    sql = "update Product set name = '%s' where id = %d" % (name, pk)

    cursor.execute(sql)


def select_one(cursor):
    sql = 'select * from Product'
    cursor.execute(sql)
    return cursor.fetchone()


def select_one_by_name(cursor, name):
    sql = 'select * from Product where name = %s'
    params = name
    cursor.execute(sql, params)
    data = cursor.fetchone()
    if data:
        print('--- 已找到名字为%s的商品. ' % data['name'])
    else:
        print('--- 名字为%s的商品已经没有了' % name)


# 修改记录
def check_update():

    with UsingMysql(log_time=True) as um:

        # 查找一条记录
        data = select_one(um.cursor)
        pk = data['id']
        print('--- 商品{0}: '.format(data))

        # 修改名字
        new_name = '单肩包'
        update_by_pk(um.cursor, new_name, pk)

        # 查看
        select_one_by_name(um.cursor, new_name)

if __name__ == '__main__':
    check_update()

