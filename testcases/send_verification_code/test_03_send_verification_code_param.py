#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc：测试请求短信验证码 sendVerificationCode 接口参数异常逻辑
#
# 影响因素：
#   1.接口 mobile 参数异常
# 检查点：
#   1.sendVerificationCode 接口返回信息
# 测试用例：
#   data/api_test_data/auth_data.yml -> test_send_verification_code

import pytest
import allure
from test_api.business.auth import send_verify_code
from testcases.conftest import auth_data


@allure.severity(allure.severity_level.NORMAL)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('请求短信验证码模块')
class TestSendVerificationCode(object):
    @allure.story('用例-参数校验')
    @allure.description('该用例对请求短信验证码接口参数进行测试')
    @allure.title('测试数据：【{mobile}, {expect_code}, {expect_msg}, {expect_result}】')
    # 参数初始化
    @pytest.mark.parametrize("mobile, expect_code, expect_msg, expect_result, status_code", auth_data['test_send_verification_code'])
    def test_send_verify_code(self, mobile, expect_code, expect_msg, expect_result, status_code):
        # 调用请求短信验证码接口
        result = send_verify_code(mobile)

        # 预期
        assert result.status_code == status_code
        assert result.json()['status'] == expect_code
        assert result.json()['msg'] == expect_msg
        assert result.json()['data'] == expect_result


if __name__ == '__main__':
    pytest.main(['-s', 'test_03_send_verification_code_param.py'])
