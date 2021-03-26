#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/26
# desc：测试注册参数异常逻辑
# 
# 影响因素：
#   1.手机号异常
#   2.联系人姓名异常
#   3.验证码异常
# 检查点：
#   1.register 接口返回信息
# 测试用例：
#   data/api_test_data/auth_data.yml -> test_register

import allure
import pytest
from test_api.business.auth import *
from testcases.conftest import auth_data


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('用户注册模块')
class TestRegister(object):
    @allure.story('用例-注册参数异常')
    @allure.description('该用例对注册接口参数进行校验')
    @allure.title('测试数据：【{nickname}, {mobile}, {verify_code}, {expect_msg}】')
    @pytest.mark.usefixtures('reset')
    @pytest.mark.parametrize('nickname, mobile, verify_code, expect_code, expect_msg, expect_data',
                             auth_data['test_register'])
    def test_register(self, nickname, mobile, verify_code, expect_code, expect_msg, expect_data):
        # 调用接口注册用户
        result_register = register(nickname, mobile, verify_code)

        # 预期
        assert result_register.json() == {
            'status': expect_code,
            'msg': expect_msg,
            'data': expect_data
        }


if __name__ == '__main__':
    pytest.main(['-s', 'test_04_register_param.py'])
