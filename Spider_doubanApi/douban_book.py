# -*- coding: utf-8 -*-
# @Time    : 18-10-2 下午10:27
# @Author  : 大长胡子
# @File    : douban_book.py
# @Software: PyCharm


import requests
import random
import xlrd

base_url = "https://api.douban.com/v2/book/isbn/:"

# UserAgent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60', 'Opera/8.0 (Windows NT 5.1; U; en)', 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36']

user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
# hearers = {"User-Agent":'Mozilla/5.0'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

proxy=[
    {'http': '106.75.164.15:3128',
     'https': '106.75.164.15:3128'},
    {'http': '115.46.97.53:8123',
     'https': '115.46.97.53:8123'},
    {'http': '123.244.148.4:32472',
     'https': '123.244.148.4:32472'},
    {'http': '60.216.101.46:59351',
     'https': '60.216.101.46:59351'},
    {'http': '123.55.152.171:33249',
     'https': '123.55.152.171:33249'},
    {'http': '182.88.129.78:8123',
     'https': '182.88.129.78:8123'},
    {'http': '116.255.176.20:8088',
     'https': '116.255.176.20:8088'},
    {'http': '110.73.2.29:8123',
     'https': '110.73.2.29:8123'},
    {'http': '110.73.7.61:8123',
     'https': '110.73.7.61:8123'},
    {'http': '111.160.236.84:39692',
     'https': '111.160.236.84:39692'},
    {'http': '119.254.94.108:51420',
     'https': '119.254.94.108:51420'},
    {'http': '110.73.2.109:8123',
     'https': '110.73.2.109:8123'},
    {'http': '121.31.101.209:8123',
     'https': '121.31.101.209:8123'},
    {'http': '182.88.214.62:8123',
     'https': '182.88.214.62:8123'},
    {'http': '182.88.190.165:8123',
     'https': '182.88.190.165:8123'},
    {'http': '175.17.204.17:36132',
     'https': '175.17.204.17:36132'},
    {'http': '182.88.14.47:8123',
     'https': '182.88.14.47:8123'},
    {'http': '117.26.40.147:29605',
     'https': '117.26.40.147:29605'},
    {'http': '180.110.4.101:808',
     'https': '180.110.4.101:808'},
    {'http': '121.228.50.32:3128',
     'https': '121.228.50.32:3128'},
    {'http': '122.96.93.158:49435',
     'https': '122.96.93.158:49435'},
    {'http': '59.58.202.246:43140',
     'https': '59.58.202.246:43140'},
    {'http': '106.56.102.10:808',
     'https': '106.56.102.10:808'},
    {'http': '114.223.245.247:808',
     'https': '114.223.245.247:808'},
    {'http': '175.148.78.122:1133',
     'https': '175.148.78.122:1133'},
    {'http': '171.39.9.70:8123',
     'https': '171.39.9.70:8123'},
    {'http': '182.240.6.90:8118',
     'https': '182.240.6.90:8118'},
    {'http': '171.37.154.242:8123',
     'https': '171.37.154.242:8123'},
    {'http': '222.182.121.81:8118',
     'https': '222.182.121.81:8118'},
    {'http': '171.12.164.113:61234',
     'https': '171.12.164.113:61234'},
    {'http': '117.24.60.249:25766',
     'https': '117.24.60.249:25766'},
    {'http': '27.153.66.119:29781',
     'https': '27.153.66.119:29781'}
    ]






def set_url():
    list = []  # 定义列表用来存放数据
    try:
        book = xlrd.open_workbook('ISBN.xlsx')  # 文件名，把文件与py文件放在同一目录下
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
            res = requests.get(url=one_url,headers={'User-Agent':random.choice(user_agent)},proxy=random.choice(proxy))
            resc = res.json()
            print(resc)
            print("1111")
    except Exception as e:
        print(e)



do_request()