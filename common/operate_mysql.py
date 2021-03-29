#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/23
# desc：mysql 数据库基本操作

import os
import pymysql
from common.set_log import logger
from common.read_data import *

# 取到 D:\code_practice\pytestSample 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 取到 D:\code_practice\pytestSample\config\setting.ini 路径
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')
mysql_info = data.load_ini(data_file_path)['mysql']

DB_CONF = {
    'host': mysql_info['MYSQL_HOST'],
    'port': int(mysql_info['MYSQL_POST']),
    'user': mysql_info['MYSQL_USER']
}


class mysqlDb(object):
    def __init__(self, use_db):
        # 通过字典拆包传递配置信息
        self.conn = pymysql.connect(**DB_CONF, db=use_db, charset='utf8')
        # 创建游标对象，并让查询结果以字典形式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 对象资源被释放时触发，在对象即将被删除时的最后操作
    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        # 检查数据库连接是否断开，如果断开了则重连
        self.conn.ping(reconnect=True)
        # 执行 sql
        self.cur.execute(sql)
        # 获取全部查询结果
        data = self.cur.fetchall()

        return data

    def execute_db(self, sql):
        try:
            # 检查数据库连接是否断开，如果断开了则重连
            self.conn.ping(reconnect=True)
            # 执行 sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info('操作Mysql出现错误，错误原因:{}'.format(e))
            # 回滚所有更改
            self.conn.rollback()

    def select(self, table, fields, bind=None, range=None):
        bind_str = None

        if bind is not None:
            bind_str = " and ".join(
                (("%s='{}'" if type(val) == str else "%s={}") % key).format(val) for (key, val) in bind.items())

        sql = "SELECT " + ",".join(fields) + " FROM " + table + ("" if bind_str is None else (" WHERE " + bind_str)) \
              + " ORDER BY id ASC" \
              + ("" if range is None else (" LIMIT %d" % (range[1] - range[0]) + " OFFSET %d" % range[0])) \
              + ";"
        print(sql)

        data = db.select_db(sql)

        return data


db = mysqlDb(mysql_info['MYSQL_SAAS_DB'])

