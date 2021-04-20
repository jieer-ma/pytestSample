#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/19
# desc：读取xx文件工具方法

import os
import yaml
import pytest
from configparser import ConfigParser
from common.set_log import logger

# 取到 D:\code\unittest 路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# 重写 ConfigParser 中的 optionxform 函数，解决传递键值对，会将键名全部转化成小写的问题
class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


# 获取各类文件数据基本方法封装
class BasicGetData(object):

    def load_yaml(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        return data

    def load_ini(self, file_path):
        logger.info('加载 {} 文件....'.format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)

        return data


# 获取特定数据方法封装
class GetData(object):

    def get_file_data(self, yaml_file_parent_dir, yaml_file_name):
        basic_data = BasicGetData()
        try:
            data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_parent_dir, yaml_file_name)
            yaml_data = basic_data.load_yaml(data_file_path)
        except Exception as ex:
            pytest.skip(str(ex))
        else:
            return yaml_data


basic_get_data = BasicGetData()
get_data = GetData()
