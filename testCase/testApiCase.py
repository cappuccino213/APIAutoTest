#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 16:44
# @Author  : Zhangyp
# @File    : testApiCase.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""测试脚本"""

import unittest
import os
from ddt import ddt, data
from common.readData import ReadData
from common.sendRequest import SendRequests
from config import DATA_TYPE, FILE_NAME


# 参数读取
def read(_type, file):
	file_path = r'%s\..\testData\%s' % (os.path.abspath(os.path.dirname(__file__)), file)
	if _type == 'Excel':
		return ReadData.read_excel(file_path)
	if _type == 'json':
		return ReadData.read_json(file_path)
	if _type == 'yaml':
		return ReadData.read_yaml(file_path)


# api_data = ReadData.read_excel(r".\testData\%s" % FILE_NAME)
api_data = read(DATA_TYPE, FILE_NAME)


@ddt  # 在测试类前必须首先声明使用 ddt.ddt
class TestCase(unittest.TestCase):
	# 测试前置方法，每个单独测试前执行
	def setUp(self) -> None:
		pass
	
	# 每个测试方法测试结束执行
	def tearDown(self) -> None:
		pass
	
	@data(*api_data)  # 加载case执行参数，list形式
	def test_api(self, _data):  # 必须方法名必须以test开头
		
		# 发送接口请求
		res = SendRequests(_data).send()
		
		# 获取预期结果
		expect_code = _data.get("expect_code")
		expect_text = _data.get("expect_res")
		
		# 实际结果
		actual_code = res.status_code
		actual_text = res.content.decode(encoding='utf-8')
		
		# 断言
		try:
			# 接口状态码
			if expect_code:
				self.assertEqual(actual_code, expect_code, msg="状态码错误,预计结果是%s，实际结果是%s" % (expect_code, actual_code))
			# 返回内容
			if expect_text:
				self.assertIn(expect_text, actual_text, msg="实际返回结果%s,不包含预期结果%s" % (actual_text, expect_text))
			# 若没有填写预期则直接断言测试失败
			if not expect_code and not expect_text:
				self.assertEqual(1, 2, msg="测试预期值未填写")
		except AssertionError as e:
			print(str(e))
			raise e


if __name__ == "__main__":
	unittest.main(verbosity=1)
