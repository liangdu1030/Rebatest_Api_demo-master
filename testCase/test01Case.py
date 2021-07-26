import json
import unittest
from common.configHttp import RunMain
from Params.params import Basic
# import paramunittest
# import geturlParams as geturlParams
# from common.Assert import Assertions
# import readExcel as readExcel

# url = geturlParams.geturlParams().get_Url()
# login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')
# @paramunittest.parametrized(*login_xls)

class testUserLogin(unittest.TestCase):
    def setParameters(self):
        self.method = Basic.method

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        # data1 = dict(urllib.parse.parse_qsl(
        #     urllib.parse.urlsplit(new_url_data).query))  # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        if self.method == 'post':
            info = RunMain().run_main(self.method, Basic.url, json.loads(Basic.data))
        elif self.method == 'get':
            info = RunMain().run_main(self.method, Basic.url, json.loads(Basic.data))
        elif self.method == 'put':
            info = RunMain().run_main(self.method, Basic.url, json.loads(Basic.data))
        ss = json.loads(info)  # 将响应转换为字典格式
        print(ss)
if __name__ == '__main__':
    unittest.main()