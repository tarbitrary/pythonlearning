#!/usr/bin/evn python	
#-*- coding: utf-8 -*-

def char2int(x):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[x]

def str2int(s):
	return reduce(lambda x, y: x*10 + y, map(str2int, s))

st = input("请输入一串数字字符:")
result = str2int(st)

print("结果为%d, 类型为%s"%(result, type(result)))
