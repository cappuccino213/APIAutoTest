#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 13:50
# @Author  : Zhangyp
# @File    : readData.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

"""读取测试数据"""
import xlrd
from common.getToken import get_token


class ReadData:
	
	# 数据存放在excel
	@staticmethod
	def read_excel(excel_file):
		with xlrd.open_workbook(excel_file) as my_book:
			sheet = my_book.sheet_by_index(0)
			# 获取总行数&总列数
			rows = sheet.nrows
			columns = sheet.ncols
			
			# 第一行为参数项
			if rows > 1:  # 判断是否有值
				keys = sheet.row_values(0)
				# 获取值case的参数
				api_data = []
				# 一行行读取
				for col in range(1, rows):
					values = sheet.row_values(col)
					for i in range(columns):
						if values[i]:
							if type(values[i]) is str:  # 去除json串中的空格和\n,主要是headers和body
								values[i] = values[i].replace("\n", "").replace(" ", "")
							if i == 0 or i == 8:  # 将浮点型转成int型
								values[i] = int(values[i])
					api_dict = dict(zip(keys, values))
					
					# 若需要token则在头部，加入token值
					token = get_token()
					if token:
						import json
						headers_dict = json.loads(api_dict['headers'])
						headers_dict['Authorization'] = token
						api_dict['headers'] = json.dumps(headers_dict)
						
					api_data.append(api_dict)
				return api_data
			else:
				print("参数值内容未填写")
				return None
	
	# 数据存放在json
	@staticmethod
	def read_json(json_file):
		pass
	
	# 数据存放在yaml
	@staticmethod
	def read_yaml(yaml_file):
		pass


if __name__ == "__main__":
	print(ReadData.read_excel(r'..\testData\sample.xlsx'))
