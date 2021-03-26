# Pytest 接口自动化

通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用Pytest作为测试执行器，使用YAML来管理测试数据，使用Allure来生成测试报告。

## 项目结构

- common ====>> 各种工具类
- config ====>> 配置文件
- core ====>> requests常用请求方法封装
- data ====>> 测试数据文件
- log ====>> 日志文件
- test_api ====>> 业务接口封装
  - api ----> 接口基础封装
  - business ----> 基础业务封装
  - scene ----> 场景封装
- testcases ====>> 测试用例

## 测试报告

使用 allure 生成测试报告，需要先安装 allure 

pycharm 中生成测试报告：

Terminal 中执行：pytest 文件 --alluredir 存放报告数据路径

Terminal 中执行：allure generate 存放报告数据路径 -o 存放allure报告路径

生成报告效果如下：

![1616747395210](C:\Users\msj\AppData\Local\Temp\1616747395210.png)







