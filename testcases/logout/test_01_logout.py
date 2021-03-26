#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/25
# desc：测试用户退出登录 logout 接口主路径
# 
# 影响因素：
#   1.用户登录状态
# 检查点：
#   1.logout 接口返回信息
# 测试用例：
#   0.调用接口退出登录，预期退出登录成功

import pytest
import requests
import allure
from test_api.business.auth import *
from core.basic_method import base_method


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户退出登录模块')
class TestLogout(object):
    @allure.story('用例-用户退出登录冒烟')
    @allure.description('该用例主要对用户退出登录进行冒烟测试')
    @allure.title('注册后退出登录成功')
    @pytest.mark.usefixtures('reset')
    def test_logout(self):
        # 注册用户
        register_result = get_verify_and_register('美洋洋', '13800000065')
        cookie_1 = base_method.get_response_cookie(register_result)
        print(cookie_1)
        assert cookie_1['SESSIONID'] is not None

        # 调用接口，用户退出登录
        result_logout = logout()
        cookie_2 = base_method.get_response_cookie(result_logout)
        print(cookie_2)

        # 预期
        assert result_logout.status_code == 200
        assert result_logout.json()['status'] == 0
        assert result_logout.json()['msg'] == 'ok'
        assert cookie_2 == {}


if __name__ == '__main__':
    # 执行用例： -s 可以把case中打印信息输出到控制台
    pytest.main(['-s', 'test_01_logout.py'])