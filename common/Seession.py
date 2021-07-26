
"""
封装获取cookie方法

"""

import requests
import os
from common.log import Logger
from Conf import Config

cookies_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Cookie_data/cookie.txt'))


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Logger().get_logger()
        self.request = requests.session()

    def Session_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        return headers

    def get_cookie(self):
        try:
            with open(cookies_path, 'r') as f:
                cookies = {}
                for line in f.read().split(';'):
                    name, value = line.strip().split('=', 1)  # 1代表只分割一次
                    cookies[name] = value
                return cookies
        except:
            self.log.error('Cookie is not exit or invalid')


if __name__ == '__main__':
    ss = Session()
    ss.get_cookie()
