#!/usr/bin/env python
#-*- coding: utf-8 -*-

def lazy_sum(*args):
	def sum():
		n = 0
		for i in args:
			n = n + i
		return n
	return sum

f = lazy_sum(*range(101))
f2 = lazy_sum(*range(101))
print("result is", f())
print("result is", f2())
print(f == f2)

"""
   返回函数里面不要引用可变参数, 因为返回函数并非立即执行,等到四个函数都返回时i
   的值变成了3,因些四个函数最后调用返回结果都是9
"""
def count():
	l = []
	for i in range(4):
		def f():
			return i*i
		l.append(f)
	return l


f1, f2, f3, f4 = count()
print(f1())
print(f2())
print(f3())
print(f4())
	

def count1():
	def a(x):
		def b():
			return x*x
		return b
	L = []
	for i in range(1, 4):
		L.append(a(i))	
	return L


f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
