#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/26
# desc：测试注册用户输入验证码逻辑：
#            1.必须注册手机号请求的短信验证码
#            2.必须使用最新请求的短信验证码注册
#            3.必须使用未失效的验证码注册
# 
# 影响因素：
#   1.请求验证码手机号
#   2.注册手机号
#   3.验证码有效性
# 检查点：
#   1.register 接口返回信息
# 测试用例：
#   0.未请求短信验证码，使用任意验证码注册，预期注册失败
#   1.请求验证码手机号和注册手机号不一致，预期注册失败
#   2.多次请求验证码，使用非最新验证码注册，预期注册失败
#   3.多次请求验证码，使用最新验证码注册，预期注册成功
#   4.使用已过期的验证码注册，预期注册失败


import pytest
import allure
import time
from test_api.business.auth import *
from core.basic_method import base_method


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户注册模块')
class TestRegister(object):
    @allure.story('用例-注册验证码')
    @allure.title('未请求验证码注册')
    @allure.description('未请求短信验证码，使用任意验证码注册，预期注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_0(self):
        # 调用接口：任意验证码
        result_register = register('美洋洋', '13800000099', '123456')

        # 获取注册后生成的cookie：用于验证当前用户登录状态
        cookie = base_method.get_response_cookie(result_register)

        assert result_register.json() == {
            'status': 149,
            'msg': '验证码不正确',
            'data': {}
        }
        assert cookie is None

    @allure.story('用例-注册验证码')
    @allure.title('请求验证码手机号和注册手机号不一致')
    @allure.description('请求验证码手机号和注册手机号不一致，预期注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_1(self):
        # 获取短信验证码
        verify_code = get_verify_code('13800000088')

        # 调用接口注册
        result_register = register('美洋洋', '13800000099', verify_code)

        assert result_register.json() == {
            'status': 149,
            'msg': '验证码不正确',
            'data': {}
        }

    @allure.story('用例-注册验证码')
    @allure.title('多次请求验证码，使用非最新验证码注册')
    @allure.description('多次请求验证码，使用非最新验证码注册，预期注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_2(self):
        # 获取短信验证码
        verify_code_1 = get_verify_code('13800000099')
        verify_code_2 = get_verify_code('13800000099')

        # 调用接口注册
        result_register = register('美洋洋', '13800000099', verify_code_1)

        assert result_register.json() == {
            'status': 149,
            'msg': '验证码不正确',
            'data': {}
        }

    @allure.story('用例-注册验证码')
    @allure.title('多次请求验证码，使用最新验证码注册')
    @allure.description('多次请求验证码，使用最新验证码注册，预期注册成功')
    @pytest.mark.usefixtures('reset')
    def test_register_3(self):
        # 获取短信验证码
        verify_code_1 = get_verify_code('13800000099')
        verify_code_2 = get_verify_code('13800000099')

        # 调用接口注册
        result_register = register('美洋洋', '13800000099', verify_code_2)

        assert result_register.json() == {
            'status': 149,
            'msg': '验证码不正确',
            'data': {}
        }

    @allure.story('用例-注册验证码')
    @allure.title('使用过期验证码注册')
    @allure.description('使用已过期的验证码注册，预期注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_4(self):
        # 获取短信验证码
        verify_code = get_verify_code('13800000099')

        # 移动时间，验证码过期(5分钟过期)
        time.sleep(60 * 5 + 1)

        # 调用接口注册
        result_register = register('美洋洋', '13800000099', verify_code)

        assert result_register.json() == {
            'status': 149,
            'msg': '验证码不正确',
            'data': {}
        }


if __name__ == '__main__':
    pytest.main(['-s', 'test_02_register_verify_code.py'])

