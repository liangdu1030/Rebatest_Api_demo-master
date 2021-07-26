#-*- coding: UTF-8 -*-
import requests
import json
import os
from common import connect_db

#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
cookies_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__), 'cookie.txt'))
def get_cookie():
    with open(cookies_path, 'r') as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)  #1代表只分割一次
            cookies[name] = value
        return cookies

#获取cookie带入请求
s = requests.Session()
url = 'https://htstoreapi-httest32.wanyol.com/xman/checkout/check-skus'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36',
    'Accept':'application/json, text/plain, */*',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    }
data = {"storeCode":"my","cartType":""}
req2 = s.post(url, json=data, headers=headers, cookies=get_cookie(), verify=False).json()
print(json.dumps(req2))
#connect_db.op_mysql.updata_one("UPDATE heytap_paycenter.merchant_transaction_payment SET `status` = 'SUCCEEDED' WHERE transaction_no='HEA2107213649000084'")