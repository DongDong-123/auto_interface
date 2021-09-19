# -*- coding: utf-8 -*-
# @Time    : 2021-09-17 22:08
# @Author  : liudongyang
# @FileName: readconfig.py
# @Software: PyCharm
# 存储数据
import configparser
import os


configfile = "config.ini"  # line
# configfile = "config_dev.ini"  # dev


curPath = os.path.dirname(os.path.realpath(__file__))
cfgPath = os.path.join(curPath, configfile)


class BaseConfig:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(cfgPath, encoding='utf-8')


class ReadMySqlConfig(BaseConfig):

    def host(self):
        return self.conf.get('mysql', 'HOST')

    def user(self):
        return self.conf.get('mysql', 'USER')

    def passwd(self):
        return self.conf.get('mysql', 'PASSWD')

    def db(self):
        return self.conf.get('mysql', 'DB')

    def port(self):
        return self.conf.get('mysql', 'PORT')


class RedisConfig(BaseConfig):
    def host(self):
        return self.conf.get('redis', 'HOST')

    def port(self):
        return self.conf.get('redis', 'PORT')

    def passwd(self):
        return self.conf.get('redis', 'PASSWD')

    def db(self):
        return self.conf.get('redis', 'DB')


class Setting(BaseConfig):
    def get_num(self):
        """设置多少条数据存储一次，若格式错误，默认10000条"""
        temp = self.conf.get('setting', 'SAVENUM')
        if temp.isalnum():
            save_num = int(temp)
        else:
            save_num = 10000
        return save_num

    def data_num(self):
        """数据数量"""
        temp = self.conf.get('setting', 'DATANUM')
        return temp

    def stif_num(self):
        temp = self.conf.get('setting', 'STIFNUM')
        return temp

    def get_save_path(self):
        temp = self.conf.get('setting', 'WINSAVEPATH')
        return temp

    def get_linux_path(self):
        temp = self.conf.get('setting', 'LINUXSAVEPATH')
        return temp

    def get_data_date(self):
        """跑批数据日期"""
        temp = self.conf.get('setting', 'DATADATE')
        return temp

    def get_file_num(self):
        """

        :return:
        """
        temp = self.conf.get('setting', 'FILENUM')
        return temp

class ReadOraclConfig(BaseConfig):
    def info(self):
        return self.conf.get('oracl', 'info')


class ReadLogPath(BaseConfig):
    def log_path(self):
        return self.conf.get('log_file', 'log_path')


if __name__ == "__main__":
    # res = ReadMySqlConfig()
    # print(res.port(),res.host(),res.user(),res.passwd(),res.db())

    res_log = ReadLogPath()
    print(res_log.log_path())