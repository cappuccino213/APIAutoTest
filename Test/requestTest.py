#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 16:45
# @Author  : Zhangyp
# @File    : requestTest.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import json
from requests import request


# headers = {"Content-Type": "application/json"}
#
# body = {
# 	"ProductName": "eWordIMCIS",
# 	"HospitalCode": "QWYHZYFZX",
# 	"RequestIP": "192.168.1.58"
# }
#
# res = request(method="post", url="http://192.168.1.8:8703/Token/RetriveInternal",
# 			  json=body, headers=headers)

# print(res.content.decode(encoding="utf-8"))


def send_request(api_data):
	method = api_data["method"]
	url = api_data["url"]
	
	# headers = api_data["headers"] if api_data["headers"] else None
	
	if api_data["headers"]:
		headers = json.loads(api_data["headers"])
	else:
		headers = None
	# params = api_data["params"] if api_data["params"] else None
	if api_data["params"]:
		params = json.loads(api_data["params"])
	else:
		params = None
	
	# body = api_data["body"] if api_data["body"] else None
	
	if api_data["body"]:
		body = api_data["body"]
	else:
		body = None
	
	# headers、params转化成dict
	# if type(headers) is not dict:
	# 	headers = json.loads(headers)
	
	# if type(params) is not dict:
	# 	headers = json.loads(params)
	
	res = request(method=method, url=url, headers=headers, params=params, data=body)
	
	return res


if __name__ == "__main__":
	# url_1 = "http://192.168.1.8:8703/Product/CheckProductRegisterStateByHospital"
	# url_2 = "http://192.168.1.8:8703/Token/RetriveInteractive"
	# 
	# headers = {"Content-Type": "application/json"}
	# 
	# body = {
	# 	"ProductName": "eWordIMCIS",
	# 	"HospitalCode": "QWYHZYFZX",
	# 	"RequestIP": "192.168.1.58"
	# }
	# 
	# param = dict(HospitalCode="QWYHZYFZX",ProductName="eWordDEP1")
	# test_data = {"method": "GET", "url": url_1,"headers":"","params":param,"body":""}
	# 
	# test_data2 = {"method": "POST", "url": url_2,"headers":headers,"params":"","body":body}
	# 
	# 
	# r=send_request(test_data2)
	# print(r.content.decode(encoding="utf-8"))
	from Test.readExcel import api_data
	
	r = send_request(api_data[3])
	res_str = r.content.decode(encoding='utf-8')
	print(res_str, type(res_str))
