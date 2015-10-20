#!/usr/bin/env python
#-- coding: utf-8 --

def write1():
	try:
		f = open("test.txt", "w")
		f.write("你好");
	finally:
		if (f):
			f.close()

def write2():
	with open("test.txt", "a") as f:
		f.write("追加内容")

write1()
write2()

