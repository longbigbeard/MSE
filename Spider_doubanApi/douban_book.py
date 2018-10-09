# -*- coding: utf-8 -*-
# @Time    : 18-10-2 下午10:27
# @Author  : 大长胡子
# @File    : douban_book.py
# @Software: PyCharm


import requests
import random
import xlrd
import time
import pymysql

base_url = "https://api.douban.com/v2/book/isbn/:"

db = pymysql.connect(host="127.0.0.1", user="root",
                         passwd="a12345",
                         db='kes_douban',
                         charset='utf8')

cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
]

#
# proxy=[
#     {'http': '106.75.164.15:3128',
#      'https': '106.75.164.15:3128'},
#     {'http': '115.46.97.53:8123',
#      'https': '115.46.97.53:8123'},
#     {'http': '123.244.148.4:32472',
#      'https': '123.244.148.4:32472'},
#     {'http': '60.216.101.46:59351',
#      'https': '60.216.101.46:59351'},
#     {'http': '123.55.152.171:33249',
#      'https': '123.55.152.171:33249'},
#     {'http': '182.88.129.78:8123',
#      'https': '182.88.129.78:8123'},
#     {'http': '116.255.176.20:8088',
#      'https': '116.255.176.20:8088'},
#     {'http': '110.73.2.29:8123',
#      'https': '110.73.2.29:8123'},
#     {'http': '110.73.7.61:8123',
#      'https': '110.73.7.61:8123'},
#     {'http': '111.160.236.84:39692',
#      'https': '111.160.236.84:39692'},
#     {'http': '119.254.94.108:51420',
#      'https': '119.254.94.108:51420'},
#     {'http': '110.73.2.109:8123',
#      'https': '110.73.2.109:8123'},
#     {'http': '121.31.101.209:8123',
#      'https': '121.31.101.209:8123'},
#     {'http': '182.88.214.62:8123',
#      'https': '182.88.214.62:8123'},
#     {'http': '182.88.190.165:8123',
#      'https': '182.88.190.165:8123'},
#     {'http': '175.17.204.17:36132',
#      'https': '175.17.204.17:36132'},
#     {'http': '182.88.14.47:8123',
#      'https': '182.88.14.47:8123'},
#     {'http': '117.26.40.147:29605',
#      'https': '117.26.40.147:29605'},
#     {'http': '180.110.4.101:808',
#      'https': '180.110.4.101:808'},
#     {'http': '121.228.50.32:3128',
#      'https': '121.228.50.32:3128'},
#     {'http': '122.96.93.158:49435',
#      'https': '122.96.93.158:49435'},
#     {'http': '59.58.202.246:43140',
#      'https': '59.58.202.246:43140'},
#     {'http': '106.56.102.10:808',
#      'https': '106.56.102.10:808'},
#     {'http': '114.223.245.247:808',
#      'https': '114.223.245.247:808'},
#     {'http': '175.148.78.122:1133',
#      'https': '175.148.78.122:1133'},
#     {'http': '171.39.9.70:8123',
#      'https': '171.39.9.70:8123'},
#     {'http': '182.240.6.90:8118',
#      'https': '182.240.6.90:8118'},
#     {'http': '171.37.154.242:8123',
#      'https': '171.37.154.242:8123'},
#     {'http': '222.182.121.81:8118',
#      'https': '222.182.121.81:8118'},
#     {'http': '171.12.164.113:61234',
#      'https': '171.12.164.113:61234'},
#     {'http': '117.24.60.249:25766',
#      'https': '117.24.60.249:25766'},
#     {'http': '27.153.66.119:29781',
#      'https': '27.153.66.119:29781'}
#     ]

json_value = []




def set_url():
    list = []  # 定义列表用来存放数据
    try:
        book = xlrd.open_workbook('aa.xlsx')  # 文件名，把文件与py文件放在同一目录下
        # print(sys.getsizeof(book))
        sheets = book.sheet_names()  # 获取所有sheet表名

        for sheet in sheets:
            sh = book.sheet_by_name(sheet)  # 打开每一张表
            row_num = sh.nrows
            print(row_num)

            for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
                row_data = sh.row_values(i)  # 按行获取excel的值
                value = base_url+(row_data[0])
                # value1 = value.replace("-","") # 用来去除isbn上面的“-”
                list.append(value)  # 将数据暂存在列表
    except:
        print("open excel file failed!")
    return list



def do_request():
    url_list = set_url() # 获取拼接后的URL列表

    try:
        for one_url in url_list:
            time.sleep(5)
            # res = requests.get(url=one_url,headers={'User-Agent':random.choice(user_agent)},proxies=random.choice(proxy))
            res = requests.get(url=one_url,headers={'User-Agent':random.choice(user_agent)})
            try:
                if res.status_code == 200:
                    resc = res.json()
                    do_json(resc)
                else:
                    with open("error_isbn_url.txt","w") as f:
                        f.write(one_url)
            except Exception as e:
                print(e)


    except Exception as e:
        print(e)


def do_json(resc):
    try:
        tags_list = []
        # print(resc)
        for i in resc['tags']:   # 取tags 放到一个列表里去
            tags_list.append(i['title'])
        value = (resc['rating']['numRaters'],resc['rating']['average'],"".join(resc['subtitle']),",".join(resc['author']),resc['pubdate'],",".join(tags_list),resc['origin_title'],resc['image'],resc['binding'],"".join(resc['translator']),\
                 resc['catalog'].replace("\n",","),resc['pages'],resc['images']['small'],resc['images']['large'],resc['images']['medium'],resc['publisher'],resc['isbn10'],resc['isbn13'],resc['title'],resc['author_intro'],resc['price'])

        sql = "INSERT INTO douban_isbn_book (rating_numTaters,rating_average,subtitle,author,pubdate,tags,origin_title,image,bindings,translator,catalog,pages,\
        images_samll,images_large,images_medium,publisher,isbn10,isbn13,title,author_intro,price)\
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, value)  # 执行sql语句
        db.commit()  # 提交
        # print('一条成功了')

    except Exception as e:
        print(e)

if __name__ == "__main__":
    do_request()
    cursor.close()  # 关闭连接
    db.close()