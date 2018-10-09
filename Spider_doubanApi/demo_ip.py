# -*- coding: utf-8 -*-
# @Time    : 18-10-3 上午11:37
# @Author  : 大长胡子
# @File    : demo_ip.py
# @Software: PyCharm
'''
    写个demo去获取一些能用的代理ip，显然是没有成功的，有空再改
'''
import requests
import urllib3
import gc  # 缓存管理
import socket
import functools
import ssl
import sys
from bs4 import BeautifulSoup


sys.path.append("..")
socket.setdefaulttimeout(20.0)
urllib3.disable_warnings = True


def cb_print(str):
    # print str
    pass

# 强制ssl使用TLSv1
def sslwrap(func):
    @functools.wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

ssl.wrap_socket = sslwrap(ssl.wrap_socket)

ip_arr = []

def get_ip_arr():
    gc.enable()
    try:
        url = 'http://vtp.daxiangdaili.com/ip/?tid=559609709731038&num=2000&delay=1&protocol=https'
        headers = {"User-Agent": "Mozilla/5.0"}
        req = urllib3.Request(url, headers=headers)
        res = urllib3.urlopen(req, timeout=20)
        res = res.read()
        ips_arr = res.split('\r\n')
        print(ips_arr)
        return ips_arr
    except Exception as e:
        cb_print('ip_arr_error:{}'.format(e))
    gc.collect()

def get_66_ip(index):
    gc.enable()
    try:
        url = 'http://www.66ip.cn/'+str(index)
        headers = {"User-Agent": "Mozilla/5.0"}
        # req = urllib3.Request(url, headers=headers)
        # res = urllib3.urlopen(req, timeout=20)
        res = requests.get(url, headers=headers)
        res = res.text()
        # print res
        soup = BeautifulSoup(res, "html.parser")
        table_arr = soup('table')
        ip_soup_arr = table_arr[len(table_arr)-1]('tr')
        ips_arr = []
        for it in ip_soup_arr:
            if it != ip_soup_arr[0]:
                ip = it('td')[0].string
                port = it('td')[1].string
                ip_port = ip + ':' + port
                ips_arr.append(ip_port)
        print(ips_arr)
        return ips_arr
    except Exception as e:
        cb_print('ip_arr_error:{}'.format(e))
    gc.collect()


def get_xici_ip():
    gc.enable()
    try:
        url = 'http://www.xicidaili.com/wn/'
        headers = {"User-Agent": "Mozilla/5.0"}
        # req = urllib3.Request(url, headers=headers)
        # res = urllib3.urlopen(req, timeout=20)
        res = requests.get(url,headers=headers)
        # res = res.read()
        soup = BeautifulSoup(res, "html.parser")
        table_arr = soup('table')
        ip_soup_arr = table_arr[len(table_arr) - 1]('tr')
        ips_arr = []
        for it in ip_soup_arr:
            if it != ip_soup_arr[0]:
                ip = it('td')[1].string
                port = it('td')[2].string
                ip_port = ip + ':' + port
                ips_arr.append(ip_port)
        return ips_arr
    except Exception as e:
        cb_print('ip_arr_error:{}'.format(e))
    gc.collect()
    pass

# 测试方法
# ip_arrs = get_xici_ip()
ip_arrs = get_66_ip(3)
print(ip_arrs)
