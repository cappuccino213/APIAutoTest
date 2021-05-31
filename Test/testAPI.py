#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 15:14
# @Author  : Zhangyp
# @File    : testAPI.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import ddt
import unittest
from Test.readExcel import api_data
from Test.requestTest import send_request


@ddt.ddt
class TestCase(unittest.TestCase):
	def setUp(self) -> None:
		# print("before test case")
		pass
	
	def tearDown(self) -> None:
		pass
	
	@ddt.data(*api_data)
	def test_token_api(self, data):
		res = send_request(data)
		
		# 预期结果状态值
		expect_code = data["expect_code"]
		# 实际结果状态值
		actual_code = res.status_code
		
		expect_text = data["expect_res"]
		actual_text = res.content.decode(encoding='utf-8')
		# actual_text = res.text
		
		try:
			# 接口返回状态断言
			self.assertEqual(actual_code, expect_code, msg="状态码错误,预计结果是%s，实际结果是%s" % (expect_code, actual_code))
			# 返回文本匹配断言
			self.assertIn(expect_text, actual_text, msg="实际返回结果%s,不包含预期结果%s" % (actual_text, expect_text))
		except AssertionError as e:
			raise e


if __name__ == "__main__":
	unittest.main(verbosity=1)
	# unittest.defaultTestLoader.discover()