# -*- coding: utf-8 -*-
# @Time    : 2021-09-17 21:18
# @Author  : liudongyang
# @FileName: send_request.py
# @Software: PyCharm
import requests


class SendRequest:
    def __init__(self):
        pass

    def get(self, **kwargs):
        """
        get 请求
        :param kwargs:
        header：
        data:

        :return:
        """
        response = requests.get(url=kwargs.get("url"), header=kwargs.get("header"))

    def post(self, **kwargs):
        """
        post 请求
        :param kwargs:
        header：
        data:
        :return:
        """
        response = requests.post(url=kwargs.get("url"), header=kwargs.get("header"), data=kwargs.get("data"))

    def put(self, **kwargs):
        """
        put 请求
        :param kwargs:
        :return:
        """

    def delete(self, **kwargs):
        """
        delete请求
        :param kwargs:
        :return:
        """

