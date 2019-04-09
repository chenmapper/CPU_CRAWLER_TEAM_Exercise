#!/usr/bin/python
# -*- coding: UTF-8 -*-

#check whether user input is num
import re
import time

number = input("請輸入一個數字，將列出可整除這個數字的integer：")



num_pattern = r'^[0-9]+$'
match = re.match(num_pattern, number.strip())

number_int = int(number)

if match:
    num = 1
    result_list = []
    while num <= number_int and num%number_int == 0:
        result_list.append(num)
        num += 1

print(result_list)