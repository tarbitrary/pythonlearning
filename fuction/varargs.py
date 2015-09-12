#!/usr/bin/env python
#-*- coding:utf-8 -*-

def test(a, b, *c):
	print(a,b)
	print("variable parameters:", end="")
	for x in c:
		print(x," ", end='')
	print()

test(1,2,*(3,4,5))


def sum(*a):
	sum = 0
	for x in a:
		sum += x
	print("result is :%d"%(sum))

sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


