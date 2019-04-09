#!/usr/bin/python
# -*- coding: UTF-8 -*-

#check whether user input is num
import re
import time

number_str = input("請輸入一個數字，將列出可整除這個數字的integer：")



num_pattern = r'^[0-9]+$'
match = re.match(num_pattern, number_str.strip())

number_int = int(number_str)

"""failure. Maybe it is local variable in while. What about variable in if or for?
if match:
    num = 1
    result_list = []
    while num <= number_int and num%number_int == 0:
        result_list.append(num)
        num += 1
"""
"""try to consider variable in whie"""
if match:




print(result_list)