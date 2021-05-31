#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 14:30
# @Author  : Zhangyp
# @File    : readExcel.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com

import xlrd

with xlrd.open_workbook(r'E:\PyProject\APIAutoTest\Test\sample.xlsx') as my_book:
	sheet = my_book.sheet_by_index(0)
	# 获取总行数&总列数
	rows = sheet.nrows
	columns = sheet.ncols
	
	# 第一行为参数项
	if rows > 1:
		keys = sheet.row_values(0)
	
	# 获取值case的参数
	api_data = []
	# 一行行读取
	for col in range(1, rows):
		values = sheet.row_values(col)
		for i in range(len(values)):
			if type(values[i]) is str:  # 去除json串中的空格和\n,主要是headers和body
				values[i] = values[i].replace("\n", "").replace(" ", "")
			if i == 0 or i == 8:  # 将浮点型转成int型
				values[i] = int(values[i])
		
		# values[i] = values[i].replace(" ", "")
		# key,value组成字典
		api_dict = dict(zip(keys, values))
		api_data.append(api_dict)

# API_DATA = api_data

if __name__ == "__main__":
	print(api_data[0])
