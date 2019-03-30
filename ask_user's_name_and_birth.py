#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""check birth format"""
import re

"""ask user's name and birth, then print those on screen"""
now_appliable_year_pattern = r"(19[0-9]{2})|(20[01][0-9])]"
def check_birth_format(birth):
    if re.match(now_appliable_year_pattern,birth):
        return int(birth)
    else:
        print("your input not matches the format. Maybe it's not in yyyy format, e.g 1996. Please enter it again!")
        input_birth = input("please input your birth:")
        check_birth_format(input_birth)


input_name = input("please input your name:")

input_birth = input("please input your birth year:")

correct_input_birth = check_birth_format(input_birth)

print("your name is: %s" %(input_name))
print("your age is: %d" %correct_input_birth)