#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/25
# desc：测试用户登录 login 接口主路径
# 
# 影响因素：
#   1.用户是否注册
#   2.登录状态
# 检查点：
#   1.login 接口返回信息
# 测试用例：
#   0.调用接口输入正确的手机号和验证码登录，预期登录成功

# todo 用户注册完成后验证码没有失效，登录时可以继续使用，下个版本修改

import pytest, allure, time
from test_api.business.auth import *
from core.basic_method import base_method


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户登录模块')
class TestLogin(object):

    @allure.story('用例-用户登录冒烟')
    @allure.description('该用例主要对用户登录进行冒烟测试')
    @allure.title('13800000099 获取验证码登录成功')
    @pytest.mark.usefixtures('reset')
    def test_login(self):
        # 用户注册并退出登录
        register_and_logout('懒洋洋', '13800000099')

        # 移动时间，用户获取短信验证码并登录
        time.sleep(61)
        verify_code = get_verify_code('13800000099')
        result_login = login('13800000099', verify_code)

        # 获取注册后生成的cookie：用于验证当前用户登录状态
        cookie = base_method.get_response_cookie(result_login)

        # 预期：注册成功
        assert result_login.status_code == 200
        assert result_login.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {}
        }
        assert cookie is not None


if __name__ == '__main__':
    pytest.main(['-s', 'test_01_login.py'])
