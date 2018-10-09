# -*- coding: utf-8 -*-
# @Time    : 18-10-8 下午3:08
# @Author  : 大长胡子
# @File    : douban_sql.py
# @Software: PyCharm


import pymysql

try:
    db = pymysql.connect(host="127.0.0.1", user="root",
                         passwd="a12345",
                         db='数据库名称',
                         charset='utf8')
except:
    print("could not connect to mysql server")


def store_to(db_name, table_name, excel_file):
    cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

    for sheet in sheets:
        sh = book.sheet_by_name(sheet)  # 打开每一张表
        row_num = sh.nrows
        print(row_num)
        list = []  # 定义列表用来存放数据
        num = 0  # 用来控制每次插入的数量
        for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sh.row_values(i)  # 按行获取excel的值
            value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], \
                     row_data[6], row_data[7], row_data[8], row_data[9], row_data[10], row_data[11], row_data[12],
                     row_data[13], row_data[14])
            list.append(value)  # 将数据暂存在列表
            num += 1
            if( num>= 10000 ):  # 每一万条数据执行一次插入
                print(sys.getsizeof(list))
                sql = "INSERT INTO " + table_name + " (time, xingbie, afdd, xzb, yzb, cfbj, jjlbmc, \
                bjlbmc, bjlxmc, bjlxxlmc, gxqymc,gxdwmc, afql, afxqxx, cjdwmc)\
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.executemany(sql, list)  # 执行sql语句

                num = 0  # 计数归零
                list.clear()  # 清空list
                print("worksheets: " + sheet + " has been inserted 10000 datas!")

    print("worksheets: " + sheet + " has been inserted " + str(row_num) + " datas!")
    db.commit()  # 提交
    cursor.close()  # 关闭连接
    db.close()