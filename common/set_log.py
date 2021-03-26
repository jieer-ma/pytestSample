#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/19
# desc：case 中添加 log 小工具

import os
import time
import logging

"""
os.path.realpath(__file__)： set_log.py 路径-> D:/code_practice/pytestSample/common/set_log.py
os.path.dirname(os.path.realpath(__file__)): set_log.py 所在上级路径 -> D:/code_practice/pytestSample/common
os.path.dirname(os.path.dirname(os.path.realpath(__file__))): common 上级路径 -> D:/code_practice/pytestSample
"""
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义 log 文件存放路径，如果没有 log 目录，则创建
LOG_PATH = os.path.join(BASE_PATH, 'log')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class  Logger():
    def __init__(self):
        self.logname = os.path.join(LOG_PATH, '{}.log'.format(time.strftime('%Y%m%d')))
        # 创建 Logger 对象
        self.logger = logging.getLogger('log')
        # 设置默认日志级别
        self.logger.setLevel(logging.DEBUG)
        # 格式化输出 log 内容：格式 [2021-03-12 12:12:12][文件名 34(行号)][日志级别]:输出信息
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        )

        # 创建FileHandler对象
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding='UTF-8')
        # 给 FileHandler 对象自定义日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 给 FileHandler 对象自定义日志格式
        self.filelogger.setFormatter(self.formater)

        # logger 日志对象加载 FileHandler 对象
        self.logger.addHandler(self.filelogger)


logger = Logger().logger


if __name__ == '__main__':
    logger.info('测试开始')
    logger.debug('测试结束')

