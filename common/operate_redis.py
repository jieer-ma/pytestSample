#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/23
# desc：redis 数据库基本操作

import os
import redis
from common.read_data import data

# 取到 D:\code_practice\pytestSample 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 取到 D:\code_practice\pytestSample\config\setting.ini 路径
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')
redis_info = data.load_ini(data_file_path)['redis']

REDIS_CONF = {
    'host': redis_info['REDIS_HOST'],
    'port': int(redis_info['REDIS_PORT']),
    'password': redis_info['REDIS_PASSWORD'],
    # 'db': 10,
}


class RedisDb(object):
    def __init__(self):
        # 连接 redis 库：Redis 取出的结果是字节，设置 decode_responses=True 即取出结果是字符串

        self.conn = redis.Redis(
            host=REDIS_CONF['host'], port=REDIS_CONF['port'], password=REDIS_CONF['password'],
            decode_responses=True
        )

    def set(self, key, value):
        self.conn.set(key, value)

    def get(self, key):
        """ 获取 redis 指定 key 的 value 值
        :param key: 要获取的redis.key
        :return:
        """
        value = self.conn.get(key)
        return value


red = RedisDb()
