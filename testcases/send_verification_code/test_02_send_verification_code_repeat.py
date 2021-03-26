#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc：测试多次请求发送验证码逻辑
#
# 影响因素：
#   0.相同手机号，请求验证码间隔时间 < 60s,调用接口请求短信验证码，预期第二次请求失败
#   1.相同手机号，请求验证码间隔时间 > 60s,调用接口请求短信验证码，预期两次均请求成功
#   2.不同手机号，请求验证码间隔时间 < 60s,调用接口请求短信验证码，预期两个手机号均请求成功
#   3.不同手机号，请求验证码间隔时间 > 60s,调用接口请求短信验证码，预期两个手机号均请求成功
#


import allure
import pytest
import time, datetime
from test_api.business.auth import send_verify_code
from testcases.conftest import auth_data
from common.sys import date_time


@allure.severity(allure.severity_level.NORMAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('请求短信验证码模块')
class TestSendVerificationCode(object):

    @allure.story('用例-多次请求验证码')
    @allure.description('相同手机号，请求验证码间隔时间 < 60s,调用接口请求短信验证码，预期第二次请求失败')
    @allure.title('相同手机号60s内重复请求验证码')
    def test_send_verification_code_0(self):
        # 第一次请求验证码
        result_1 = send_verify_code('13800000058')
        # 预期
        assert result_1.json()['status'] == 0
        assert result_1.json()['msg'] == 'ok'

        # 第二次请求验证码
        result_2 = send_verify_code('13800000058')
        # 预期
        assert result_2.json()['status'] == 120
        assert result_2.json()['msg'] == '验证码发送太频繁'

    @allure.story('用例-多次请求验证码')
    @allure.description('相同手机号大于60s重复请求验证码')
    @allure.title('测试数据：【13800000059】')
    def test_send_verification_code_1(self):
        # 第一次请求验证码
        result_1 = send_verify_code('13800000059')
        # 预期
        assert result_1.json()['status'] == 0
        assert result_1.json()['msg'] == 'ok'

        # 第二次请求验证码
        time.sleep(61)
        result_2 = send_verify_code('13800000059')
        # 预期
        assert result_2.json()['status'] == 0
        assert result_2.json()['msg'] == 'ok'

    @allure.story('用例-多次请求验证码')
    @allure.description('不同手机号，请求验证码间隔时间 < 60s,调用接口请求短信验证码，预期两个手机号均请求成功')
    @allure.title('不同手机号60s内重复请求验证码')
    def test_send_verification_code_2(self):
        # 第一次请求验证码
        result_1 = send_verify_code('13800000060')
        # 预期
        assert result_1.json()['status'] == 0
        assert result_1.json()['msg'] == 'ok'

        # 第二次请求验证码
        result_2 = send_verify_code('13800000061')
        # 预期
        assert result_2.json()['status'] == 0
        assert result_2.json()['msg'] == 'ok'

    @allure.story('用例-多次请求验证码')
    @allure.description('不同手机号，请求验证码间隔时间 > 60s,调用接口请求短信验证码，预期两个手机号均请求成功')
    @allure.title('不同手机号大于60s请求验证码')
    def test_send_verification_code_3(self):
        # 第一次请求验证码
        result_1 = send_verify_code('13800000062')
        # 预期
        assert result_1.json()['status'] == 0
        assert result_1.json()['msg'] == 'ok'

        # 第二次请求验证码
        time.sleep(61)
        result_2 = send_verify_code('13800000063')
        # 预期
        assert result_2.json()['status'] == 0
        assert result_2.json()['msg'] == 'ok'


if __name__ == '__main__':
    pytest.main(['-s', 'test_02_send_verification_code_repeat.py'])
