#! /usr/bin/python
# -*- coding: UTF-8 -*-



from sqlal_comm import Session, Product, UsingAlchemy


# 测试获取一条记录
def check_it():

    session = Session()

    result = session.query(Product).first()
    if result is None:
        session.commit()
        return None

    session.commit()
    session.close()
    print('-- 得到记录: {0}'.format(result))


# 测试获取一条记录
def check_it_2():

    with UsingAlchemy() as ua:

        result = ua.session.query(Product).first()
        print('-- 得到记录: {0}'.format(result))

if __name__ == '__main__':
    check_it()
    check_it_2()