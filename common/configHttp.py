#coding:utf-8
import jsonpath
import requests
import json
from common.Seession import Session
from common.log import Logger


class RunMain:

    def __init__(self):
        self.log = Logger().get_logger()
        self.send_headers = Session.Session_headers(self)
        self.send_cookies = Session.get_cookie(self)

    def get_json_value(self, json_data, key_name):
        # 获取到json中任意key的值,结果为list格式
        # key的值不为空字符串或者为empty（用例中空固定写为empty）返回对应值，否则返回empty
        key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
        return key_value

    def send_post(self, url, data):
        result = requests.post(url=url, json=data, headers=self.send_headers, cookies=self.send_cookies).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_put(self, url, data):
        result = requests.put(url=url, json=data, headers=self.send_headers, cookies=self.send_cookies).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, json=data, headers=self.send_headers, cookies=self.send_cookies).content.decode(encoding='utf8')
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        elif method == 'put':
            result = self.send_get(url, data)
        else:
            self.log.error('Method is false or nonexistent')
        return result


if __name__ == '__main__':
    result1 = RunMain().run_main('post', 'https://htstoreapi-httest32.wanyol.com/xman/checkout/calc',
                                 {"store":"my","cartType":"quick","shippingAddressId":620})