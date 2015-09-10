#!/usr/bin/env python
#-*- coding:utf-8 -*-

a=input("please input a word:")
length = len(a)
for i in range(0,length):
	print(hex(ord(a[i])),end="")
