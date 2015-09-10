#!/usr/bin/env python 
#-*- coding:utf-8 -*-

def power(a, b = 2):
	sum = 1
	while b > 0:
		sum *= a
		b -= 1
	return sum

a = input("请输入a的值:")
b = input("请输入b的值:")
if len(b) == 0:
	print(power(int(a)))
else:
	print(power(int(a), int(b)))
	
