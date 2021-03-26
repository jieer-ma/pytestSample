#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/19
# desc：读取xx文件工具方法

from configparser import ConfigParser
from common.set_log import logger
import yaml


# 重写 ConfigParser 中的 optionxform 函数，解决传递键值对，会将键名全部转化成小写的问题
class MyConfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData(object):

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


data = ReadFileData()
