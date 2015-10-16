#!/usr/bin/env python
#-- coding: utf-8 --

"""
 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后（如果没有遇到异常且except语句后有else语句则会执行else后面的）如果有finally语句块，则执行finally语句块，至此，执行完毕。
"""
try:
	r = 10 / 1
except BaseException as e:
	print(e)
else:
	print("no exception")
finally:
	print("the end")



