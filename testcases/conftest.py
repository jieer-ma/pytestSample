#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/20
# desc：共享模块：初始化测试环境、制造测试数据


import os
import pytest
from common.read_data import data
from common.operate_mysql import db

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# 获取测试数据
def get_data(yaml_file_parent_dir, yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_parent_dir, yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


# 获取测试数据文件数据
api_data = get_data('api_test_data', 'product_data.yml')
auth_data = get_data('api_test_data', 'auth_data.yml')


# 获取数据库下所有表
def get_all_tables():
    all_tables = db.select_db('SHOW TABLES;')
    table = []
    for x in range(0, len(all_tables)):
        table += list(all_tables[x].values())

    return table


# 当用例中函数添加 reset 参数时，会执行 reset 函数内容
@pytest.fixture(scope='function')
# 重置数据库: 将所有表数据清空，保证每个case之间数据独立
def reset():
    tables = get_all_tables()
    for x in range(0, len(tables)):
        db.execute_db('DELETE FROM ' + tables[x] + ';')