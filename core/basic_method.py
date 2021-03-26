#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/19
# desc：python 基础 request 方法封装

import pytest
import requests


class BasicMethod(object):

    def post_method(self, url, headers, data):
        # 遇到request的ssl验证，若想跳过不验证，则设置 verify=False 即可
        response = requests.post(url, headers=headers, data=data, verify=False)

        return response

    def get_method(self, url, headers, data=None):
        # 遇到request的ssl验证，若想跳过不验证，则设置 verify=False 即可
        response = requests.get(url, headers=headers, data=data, verify=False)
        return response

    def request(self, method, url, headers, data=None):

        res = None

        if method == 'POST':
            res = self.post_method(url, headers, data)
        elif method == 'GET':
            res = self.get_method(url, headers, data)

        # 暂时将该段代码注释掉，底层方法直接 json 后，无法校验 status_code
        '''
        if res:
            # 将响应数据以json数据格式返回
            return res.json()

        return None
        '''

        return res

    def get_response_cookie(self, result):
        """
        获取接口 response.cookie
        :param result:
        :return:
        """
        cookie = requests.utils.dict_from_cookiejar(result.cookies)

        return cookie


base_method = BasicMethod()