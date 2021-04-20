#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/26
# desc：finadv_saas 数据库表操作封装


from common.operate_mysql import db_saas


class finadvSaasDB(object):
    def getUser(self, fields, bind=None, range=None, expect_result=None):
        data = db_saas.select('user', fields, bind, range)

        assert data == expect_result

    def getAuthMobile(self, fields, bind=None, range=None, expect_result=None):
        data = db_saas.select('auth_mobile', fields, bind, range)

        assert data == expect_result


user_db = finadvSaasDB()
