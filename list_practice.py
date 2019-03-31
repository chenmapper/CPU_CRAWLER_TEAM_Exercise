#!/usr/bin/python
# -*- coding: UTF-8 -*-

s1 = [1, 3, 5, 7, 9]
print(s1)

s1.append(10)
print(s1)

s2 = [2,4,6,8,10]
print(s2)

s2.insert(0,0)
print(s2)

print(10 in s1)

print("the intersection of s1 and s2 is: " + str(list(set(s1)&set(s2))))

print("the union of s1 and s2 is: " + str(list(set(s1)|set(s2))))

print(s1)
print(s2)