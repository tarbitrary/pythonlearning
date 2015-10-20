#!/usr/bin/env python
#-- coding: utf-8 --


def read1():
	# f必须关闭,python中try catch是没有作用域的，所以f在finally里面可以直接用，这一点跟java中有区别
	try:
		f = open("text.txt", "r")
		print(f.read())
	finally:
		if (f):
			f.close()


	
def read2():
	#为避免繁琐的try catch finally字段来关闭io,python提供了with open的方法来调用，好处是不用手动关闭io流
	with open("text.txt", "r") as f:
		print(f.read())

def read3():
	with open("text.txt", "r") as f:
		for line in f.readlines():
			print(line.strip())

read1()
read2()
read3()
