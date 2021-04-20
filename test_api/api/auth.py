#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc： saas 用户注册/登录相关接口基础封装

import json
import os
from common.read_data import *
from core.basic_method import base_method

# 取到 D:\code\unittest 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# 取到 D:\code\unittest\config\setting.ini 路径
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')
auth_api_root_url = basic_get_data.load_ini(data_file_path)['host']['auth_api_root_url']


class AllApi(object):

    def send_verification_code(self, headers, send_data):
        url = auth_api_root_url + '/mobile/sendVerificationCode'
        # json.dumps() 将字典转换成字符串  json.load() 将字符串转化成字典
        result = base_method.request('POST', url, headers, json.dumps(send_data))

        return result

    def register(self, headers, send_data):
        url = auth_api_root_url + '/mobile/register'
        result = base_method.request('POST', url, headers, json.dumps(send_data))

        return result

    def login(self, headers, send_data):
        url = auth_api_root_url + '/mobile/login'
        result = base_method.request('POST', url, headers, json.dumps(send_data))

        return result

    def logout(self, headers):
        url = auth_api_root_url + '/logout'
        result = base_method.request('POST', url, headers)

        return result


auth_api = AllApi()
