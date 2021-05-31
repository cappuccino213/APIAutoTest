#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 10:51
# @Author  : Zhangyp
# @File    : getToken.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import json
from requests import post
from config import TOKEN_FLAG, TOKEN_INFO


# 根据token标志判断获取token
def get_token():
	if TOKEN_FLAG:
		res = post(TOKEN_INFO['host'], json=TOKEN_INFO['body'])
		res_dict = json.loads(res.content.decode(encoding='utf-8'))
		return res_dict['token']
	else:
		return None


if __name__ == '__main__':
	print(get_token())
