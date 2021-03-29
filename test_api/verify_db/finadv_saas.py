#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/26
# desc：finadv_saas 数据库表操作封装


from common.operate_mysql import db


class finadvSaasDB(object):

    def getUser(self, fields, bind=None, range=None, expect_result=None):
        data = db.select('user', fields, bind, range)

        if data == ():
            data = []

        assert data == expect_result

    def getAuthMobile(self, fields, bind=None, range=None, expect_result=None):
        data = db.select('auth_mobile', fields, bind, range)

        if data == ():
            data = []

        assert data == expect_result


user_db = finadvSaasDB()
