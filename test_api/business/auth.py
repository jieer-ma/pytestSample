#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/24
# desc：saas 用户注册/登录相关基础业务封装


from test_api.api.auth import auth_api
from common.operate_redis import red


# ---------------------------------- 单一接口基础封装 ---------------------------------#
def send_verify_code(mobile):
    """ 请求短信验证码
    :param mobile: 请求短信验证码手机号
    """

    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    send_data = {
        'mobile': mobile
    }

    res = auth_api.send_verification_code(headers, send_data)

    return res


def register(nickname, mobile, verify_code):
    """ saas 注册用户
    :param nickname: 联系人姓名
    :param mobile: 联系人手机号
    :param verify_code: 短信验证码
    """

    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    send_data = {
        'nickname': nickname,
        'mobile': mobile,
        'verificationCode': verify_code
    }

    res = auth_api.register(headers, send_data)

    return res


def login(mobile, verify_code):
    """ saas 用户登录
    :param mobile: 登录手机号
    :param verify_code: 短信验证码
    """

    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    send_data = {
        'mobile': mobile,
        'verificationCode': verify_code
    }

    res = auth_api.login(headers, send_data)

    return res


def logout():
    """ saas 用户退出登录
    """

    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }

    res = auth_api.logout(headers)

    return res


# ---------------------------------- 基础业务封装 ------------------------------------#
def get_verify_code(mobile):
    """ 获取短信验证码
    :param mobile:
    :return:
    """
    send_verify_code(mobile)
    verify_code = red.get('Auth:VerificationCode:' + mobile)

    return verify_code


def get_verify_and_register(user_name, mobile):
    """ 获取短信验证码并注册
    :param user_name:
    :param mobile:
    :return:
    """
    # 获取短信验证码
    verify_code = get_verify_code(mobile)
    # 注册用户
    register_result = register(user_name, mobile, verify_code)

    return register_result


def register_and_logout(user_name, mobile):
    """ 获取短信验证码并注册
        :param user_name:
        :param mobile:
        :return:
        """
    # 获取短信验证码并注册
    get_verify_and_register(user_name, mobile)
    # 用户退出登录
    logout()
