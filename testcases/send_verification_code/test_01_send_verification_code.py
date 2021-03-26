#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc：测试请求短信验证码 sendVerificationCode 接口主路径
#
# 影响因素：
#   1.mobile 参数异常
#   2.相同手机号请求验证码时间间隔
#   3.多个手机号请求验证码
# 检查点：
#   1.sendVerificationCode 接口返回信息
# 测试用例：
#   0.调用接口输入正确手机号请求验证码，预期请求成功

import datetime
import allure
import pytest
from test_api.business.auth import send_verify_code

'''
* 设置用例级别
 *  blocker(阻塞缺陷，功能未实现，无法下一步) 
 *  critical(严重缺陷，功能点未实现) 
 *  normal(一般缺陷，边界情况，格式错误) 
 *  minor(次要缺陷，界面缺陷与ui不符)
 *  trivial(轻微缺陷，必须项无提示或提示不准确)
'''


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('saas 用户注册/登录功能测试')
@allure.feature('请求短信验证码模块')
class TestSendVerificationCode(object):

    @allure.story('用例-请求短信验证码冒烟')
    @allure.description('冒烟测试：调用接口输入正确手机号请求验证码，预期请求成功')
    @allure.title('13800000099 请求短信验证码成功')
    @pytest.mark.usefixtures('reset')
    def test_send_verification_code(self):
        # 调用请求短信验证码接口：传入正确的手机号
        result = send_verify_code('13800000055')

        # 预期请求成功
        assert result.status_code == 200
        assert result.json()['status'] == 0
        assert result.json()['msg'] == 'ok'
        assert result.json()['data'] == {}


if __name__ == '__main__':
    pytest.main(['-s', 'test_01_send_verification_code.py'])
