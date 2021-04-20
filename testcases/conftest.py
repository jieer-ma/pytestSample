#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MSJ
# date: 2021/3/20
# desc：共享模块：初始化测试环境、制造测试数据

from common.read_data import *
from common.operate_mysql import *

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 取到 D:\code\unittest\config\setting.ini 路径
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')
mysql_info = basic_get_data.load_ini(data_file_path)['mysql']


# 获取测试数据文件数据
api_data = get_data.get_file_data('api_test_data', 'product_data.yml')
auth_data = get_data.get_file_data('api_test_data', 'auth_data.yml')


# 获取 finadv_saas 数据库下所有表
def get_saas_tables():
    all_tables = db_saas.select_db('SHOW TABLES;')
    table = []
    for x in range(0, len(all_tables)):
        table += list(all_tables[x].values())

    return table


# 清空 finadv_saas 数据库下所有表数据
def reset_saas():
    tables = get_saas_tables()
    # product_supply_chain 是一个临时表，临时表中的元素会根据主表自动变，不需要手工删除
    tables.remove('product_supply_chain')
    for x in range(0, len(tables)):
        db_saas.execute_db('DELETE FROM ' + tables[x] + ';')


# 获取 finadv_user_center 数据库下所有表
def get_user_center_tables():
    all_tables = db_user_center.select_db('SHOW TABLES;')
    table = []
    for x in range(0, len(all_tables)):
        table += list(all_tables[x].values())

    return table


# 清空 finadv_user_center 数据库下所有表数据
def reset_user_center():
    tables = get_user_center_tables()
    for x in range(0, len(tables)):
        db_user_center.execute_db('DELETE FROM ' + tables[x] + ';')


# 当用例中函数添加 reset 参数时，会执行 reset 函数内容
@pytest.fixture(scope='function')
# 重置数据库: 将所有表数据清空，保证每个case之间数据独立
def reset():
    reset_saas()
    reset_user_center()