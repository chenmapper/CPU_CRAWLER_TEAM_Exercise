#!/usr/bin/python
# -*- coding: UTF-8 -*-

w1=list(input("請輸入一個字串"))

l1=[1,2,3,4,5]

w2=w1
print(type(w1))
print(type(w2))
print(id(w1))
print(id(w2))

l2=l1

print(w1)
print(w2)

print(l1)
print(l2)

w3=reversed(w2)


l2.reverse()
print(w1)
print(w2)
print(w3)
print([x for x in w3])

print(l1)
print(l2)

w1=''.join(w1)
w2=''.join(w2)

print(w1)
print(w2)

print(l1)
print(l2)

if w1==w2:
    print("可逆")
else:
    print("不可逆")