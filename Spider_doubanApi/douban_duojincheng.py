# -*- coding: utf-8 -*-
# @Time    : 18-10-3 下午12:08
# @Author  : 大长胡子
# @File    : douban_duojincheng.py
# @Software: PyCharm

from douban_book import do_request

import multiprocessing
# import SqlOperation #我的数据库操作类
import time

#我的每个进程内，执行id的顺序
def worker(num):
    thread_index = SqlOperation.get_thread_index_id(num)
    #查询当前第 num 个进程已经爬取到最大 id
    process_index = num*50000+1000000
    # print str(process_index) + ':' + str(thread_index)
    if process_index < thread_index:
        process_index = thread_index
    #获取当前第 num 个进程，应该开始爬去数据的起始 id
    Crawler.start_crawler(process_index, num)
    #开始爬取数据，进程为第 num 个，起始id为 process_index

done_id_arr = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 23, 25, 26, 27, 28, 30, 32, 34, 36, 38, 39, 40]
#已完成爬取数据的进程id数组，从数据里查到的，但因为每次启动程序，此处只执行一次，就直接硬编码，没有写自动获取的方法

if __name__ == '__main__':
    jobs = []
    # Crawler.ips = Crawler.get_ip_arr()
    #获取代理ip组
    # print Crawler.ips
    # Crawler.test_ip(1000007)
    for i in range(11, 200):
        if i in done_id_arr:
            # 如果 第 i 个进程的数据已经爬完了，即 i 在 done_id_arr中，
            # 说明此进程没有开的必要了，可节省相应资源
            pass
        else:
            # 单开进程，爬取第 i 个id组的数据
            p = multiprocessing.Process(target=worker, args=(i,))
            jobs.append(p)
            p.start()
