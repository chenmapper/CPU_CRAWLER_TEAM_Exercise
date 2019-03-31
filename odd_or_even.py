#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""check whether user input is num"""
import re

num_pattern = r'^[0-9]+$'

while True:
    num_str = input("請輸入一個數字：")
    if re.match(num_pattern, num_str.strip()):
        if int(num_str) % 2:
            print("奇數")
        else:
            print("偶數")
        break
    else:
        print("請重新輸入！")
