#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/26
# desc：重复注册用户逻辑：注册过的用户(手机号注册过)不能再次注册
# 
# 影响因素：
#   1.手机号重复
#   2.联系人姓名重复
# 检查点：
#   1.register 接口返回信息
# 测试用例：
#   0.重复注册：手机号和姓名均相同，预期第二次注册失败
#   1.重复注册：手机号相同，姓名不同，预期第二次注册失败
#   2.重复注册：手机号不同，姓名相同，预期两次均注册成功

import pytest
import allure
from test_api.business.auth import *
from testcases.register.conftest import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户注册模块')
class TestRegister():
    @allure.story('用例-重复注册')
    @allure.title('重复注册：手机号/姓名均相同')
    @allure.description('重复注册：手机号和姓名均相同，预期第二次注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_0(self):
        # 请求验证码并注册
        verify_code_1 = get_verify_code('13800000099')
        result_register_1 = register('美洋洋', '13800000099', verify_code_1)

        # 预期
        assert result_register_1.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {
                'agent_qr_code': AGENT_QR_CODE
            }
        }

        # 请求验证码并注册
        verify_code_2 = get_verify_code('13800000099')
        result_register_2 = register('美洋洋', '13800000099', verify_code_2)

        # 预期
        assert result_register_2.json() == {
            'status': 140,
            'msg': '手机号已被注册',
            'data': {}
        }

    @allure.story('用例-重复注册')
    @allure.title('重复注册：手机号相同，姓名不同')
    @allure.description('重复注册：手机号相同，姓名不同，预期第二次注册失败')
    @pytest.mark.usefixtures('reset')
    def test_register_1(self):
        # 请求验证码并注册
        verify_code_1 = get_verify_code('13800000099')
        result_register_1 = register('美洋洋', '13800000099', verify_code_1)

        # 预期
        assert result_register_1.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {
                'agent_qr_code': AGENT_QR_CODE
            }
        }

        # 请求验证码并注册
        verify_code_2 = get_verify_code('13800000099')
        result_register_2 = register('懒洋洋', '13800000099', verify_code_2)

        # 预期
        assert result_register_2.json() == {
            'status': 140,
            'msg': '手机号已被注册',
            'data': {}
        }

    @allure.story('用例-重复注册')
    @allure.title('重复注册：手机号不同，姓名相同')
    @allure.description('重复注册：手机号不同，姓名相同，预期两次均注册成功')
    @pytest.mark.usefixtures('reset')
    def test_register_2(self):
        # 请求验证码并注册
        verify_code_1 = get_verify_code('13800000099')
        result_register_1 = register('美洋洋', '13800000099', verify_code_1)

        # 预期
        assert result_register_1.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {
                'agent_qr_code': AGENT_QR_CODE
            }
        }

        # 请求验证码并注册
        verify_code_2 = get_verify_code('13800000098')
        result_register_2 = register('美洋洋', '13800000098', verify_code_2)

        # 预期
        assert result_register_2.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {
                'agent_qr_code': AGENT_QR_CODE
            }
        }


if __name__ == '__main__':
    pytest.main(['-s', 'test_03_register_repeat.py'])

