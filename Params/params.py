#coding:utf-8


"""
定义所有测试数据

"""
import os
from Params import tools
from common.log import Logger
log = Logger().get_logger()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Basic:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/Basic.yaml')
    params = get_parameter('Basic')
    method = []
    url = []
    data = []
    for i in range(0, len(params)):
        method.append(params[i]['method'])
        url.append(params[i]['url'])
        data.append(params[i]['data'])


class Collections:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/Collections.yaml')
    params = get_parameter('Collections')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])


class Personal:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/Personal.yaml')
    params = get_parameter('Personal')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Login:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/Login.yaml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
if __name__ == '__main__':
    print(Basic.method)