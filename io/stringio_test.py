#!/usr/bin/env python
# -- coding: utf-8 --

from io import StringIO

s = StringIO()
s.write("hello,")
s.write("tarbitrary!")
#getvalue()方法用于获得写入后的str。
print(s.getvalue())

"""
要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
"""
f = StringIO("hello\ntarbitrary\n!")
while True:
	l = f.readline()
	if l == '':
		break
	print(l.strip())

