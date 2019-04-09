#!/usr/bin/python
# -*- coding: UTF-8 -*-

#check whether user input is num
import re
import time

number_str = input("請輸入一個數字，將列出可整除這個數字的integer：")



num_pattern = r'^[0-9]+$'
match = re.match(num_pattern, number_str.strip())

number_int = int(number_str)

"""first failure debug long time finding num%number_int -> number_int%num"""
result_list = [x for x in range(1,number_int+1) if number_int%x==0]

print(result_list)