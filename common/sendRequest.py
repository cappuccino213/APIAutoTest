#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 14:22
# @Author  : Zhangyp
# @File    : sendRequest.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import json
from requests import request, RequestException


class SendRequests:
	"""
	data:字典参数
	"""
	
	def __init__(self, data):
		self.url = data.get("url")
		self.method = data.get("method")
		self.headers = data.get("headers")
		self.body = data.get("body")
		self.params = data.get("params")
	
	def send(self):
		# 将读取json串转化成dict
		if self.headers:
			self.headers = json.loads(self.headers)
		if self.params:
			self.params = json.loads(self.params)
		try:
			return request(method=self.method, url=self.url, headers=self.headers, params=self.params, data=self.body)
		except RequestException as e:
			print("请求异常：%s" % e)
			return None


if __name__ == "__main__":
	from common.readData import ReadData
	
	test_data = ReadData.read_excel(r'..\testData\sample.xlsx')
	r = SendRequests(test_data[0])
	res_str = r.send().content.decode(encoding='utf-8')
	print(res_str, type(res_str))
