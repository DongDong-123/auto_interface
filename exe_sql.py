# -*- coding: utf-8 -*-
# @Time    : 2021-09-17 22:05
# @Author  : liudongyang
# @FileName: exe_sql.py
# @Software: PyCharm
import pymysql
import time
from readconfig import ReadMySqlConfig
import os


class ExeSql:
    def __init__(self):
        self.host = ReadMySqlConfig().host()
        self.user = ReadMySqlConfig().user()
        self.passwd = ReadMySqlConfig().passwd()
        self.port = int(ReadMySqlConfig().port())
        self.db = ReadMySqlConfig().db()
        self.day = time.strftime('%Y-%m-%d', time.localtime())

    def exe_sql(self, sql):
        conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port, db=self.db,
                                charset="utf8")
        cur = conn.cursor()
        time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        cur.execute(sql)
        conn.commit()
        # print("{} 已执行".format(sql))
        res = cur.fetchall()
        if not os.path.exists(os.path.join(os.getcwd(), 'logs')):
            os.mkdir(os.path.join(os.getcwd(), 'logs'))
        with open('logs\{}.log'.format(self.day), '+a', encoding='utf-8') as f:
            f.write('{}  {}  execute sql {}'.format(time_now, self.db, sql) + '\n')
            f.write('{}  =={} result== '.format(time_now, self.db) + str(res) + '\n')
        cur.close()
        conn.close()
        return res