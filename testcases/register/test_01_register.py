#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc：测试注册 saas 用户 register 接口主路径
#
# 影响因素：
#   1.注册验证码
#   2.注册手机号(唯一)
# 检查点：
#   1.register 接口返回信息
# 测试用例：
#   0.输入正确的手机号，用户名，验证码注册，预期注册成功


import allure
import pytest
from core.basic_method import base_method
from test_api.business.auth import *
from testcases.register.conftest import *
from common.operate_mysql import db


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户注册模块')
class TestRegister(object):
    @allure.story('用例-注册冒烟')
    @allure.description('该用例主要对用户注册进行冒烟测试')
    @allure.title('美洋洋，13800000088 注册成功')
    @pytest.mark.usefixtures('reset')
    def test_register(self):
        # 获取短信验证码
        verify_code = get_verify_code('13800000088')
        # 调用接口注册用户
        result_register = register('美洋洋', '13800000088', verify_code)

        # 获取注册后生成的cookie：用于验证当前用户登录状态
        cookie = base_method.get_response_cookie(result_register)

        # 预期：注册成功&&注册成功后会将cookie记录
        assert result_register.status_code == 200
        assert cookie is not None
        assert result_register.json() == {
            'status': 0,
            'msg': 'ok',
            'data': {
                'agent_qr_code': AGENT_QR_CODE
            }
        }

        """
        data = db.select_db('SELECT * FROM user;')
        assert data == [
            {
                'id': 23, 'nickname': '美洋洋', 'type': 1, 'status': 1,
                'last_login': datetime.datetime.now(),
                'create_time': datetime.datetime.now(),
                'addition': '{}'
            }
        ]
        print(data)
        """


if __name__ == '__main__':
    pytest.main(['-s', 'test_01_register.py'])

    '''
        生成 allure 报告步骤：
        控制台执行命令生成报告数据：pytest 文件 --alluredir 存放报告数据路径
        控制台执行命令转换成allure 报告：allure generate 存放报告数据路径 -o 存放allure报告路径
    '''
