#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 16:39
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import unittest
from BeautifulReport import BeautifulReport
from config import SCRIPT, REPORT_NAME, GENERATE_MODE, DESCRIPTION, THEME
import time

if __name__ == "__main__":
	# 加载测试脚本
	test_suite = unittest.defaultTestLoader.discover(r'./testCase', pattern=SCRIPT)
	# 获取测试结果
	result = BeautifulReport(test_suite)
	# 生成测试报告
	# result.report(filename='testReport', description='测试报告', report_dir='./report', theme='theme_cyan')
	report_file = REPORT_NAME if GENERATE_MODE == 'OVERWRITE' else REPORT_NAME + time.strftime("%Y%m%d%H%M%S",
																							   time.localtime())
	result.report(filename=report_file, description=DESCRIPTION, report_dir='./report', theme=THEME)
