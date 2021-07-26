

from configparser import ConfigParser
from common.log import Logger
import os


class Config:

    #title:
    TITLE_heytap = "pymysql"

    #values:
    Values_host = 'host'
    Values_port = 'port'
    Values_user = 'user'
    Values_passwd = 'passwd'
    Values_db = 'db'
    Values_charset = 'charset'

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Logger().get_logger()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.conf_path_cookie = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                             '../common/Cookie_data/cookie.txt')
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')
        self.send_Values_host = self.get_conf(Config.TITLE_heytap, Config.Values_host)
        self.send_Values_port = self.get_conf(Config.TITLE_heytap, Config.Values_port)
        self.send_Values_user = self.get_conf(Config.TITLE_heytap, Config.Values_user)
        self.send_Values_passwd = self.get_conf(Config.TITLE_heytap, Config.Values_passwd)
        self.send_Values_charset = self.get_conf(Config.TITLE_heytap, Config.Values_charset)


    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    print(Config.s)