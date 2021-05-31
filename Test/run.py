#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 15:30
# @Author  : Zhangyp
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import unittest
from BeautifulReport import BeautifulReport as bf

if __name__ == "__main__":
	# 加载测试脚本
	test_suite = unittest.defaultTestLoader.discover(r'E:\PyProject\APIAutoTest\Test',pattern='test*.py')
	result = bf(test_suite)
	result.report(filename='testReport', description='测试deafult报告', report_dir='report', theme='theme_cyan')
