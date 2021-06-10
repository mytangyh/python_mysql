#! /usr/bin/python
# -*- coding: UTF-8 -*-


from pymysql_comm import UsingMysql


def fetch_page_data(cursor, pk, page_size, skip):
    sql = 'select * from Product where id > %d limit %d,%d' % (pk, skip, page_size)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print('-- 总数: %d' % len(data_list))
    print('-- 数据: {0}'.format(data_list))
    return data_list


# 查找
def check_page():

    with UsingMysql(log_time=True) as um:

        page_size = 10
        pk = 500

        for page_no in range(1, 6):

            print('====== 第%d页数据' % page_no)
            skip = (page_no - 1) * page_size

            fetch_page_data(um.cursor, pk, page_size, skip)


if __name__ == '__main__':
    check_page()

