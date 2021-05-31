#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 16:39
# @Author  : Zhangyp
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""测试数据设置"""
# 读取的数据类型，支持Excel、json、yaml
DATA_TYPE = 'Excel'

# 文件名
FILE_NAME = 'sample.xlsx'

"""API设置"""
# 当TOKEN_FLAG=1时表示api调用需要token，再调用时会根据token_info获取对应的token信息，为0时表示api不需要token
TOKEN_FLAG = 0
TOKEN_INFO = dict(host='http://192.168.1.18:8709/Token/RetriveInternal',
				  body=dict(ProductName='eWordIMCIS', HospitalCode='QWYHZYFZX', RequestIP='192.168.1.58'))

"""测试用例设置"""
# 测试的脚本,如testA*.py,表示以testA开头的脚本，但是测试用例必须以test为开头的
SCRIPT = 'testA*.py'

"""测试报告设置"""
# 报告生成方式：ADD,OVERWRITE
GENERATE_MODE = 'ADD'
# 报告文件名
REPORT_NAME = 'TestAPIReport'

# 测试报告名称
DESCRIPTION = 'tokenAPI测试报告'
# 测试报告主题，可选主题：theme_default,theme_cyan,theme_memories,theme_candy
THEME = 'theme_candy'


