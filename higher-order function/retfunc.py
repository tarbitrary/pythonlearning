#!/usr/bin/env python	
#--  coding: utf-8 --

def count():
	def a(x):
		def b():
			return x*x
		return b
	L = []
	for i in range(1, 4):
		L.append(a(i))	
	return L


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
