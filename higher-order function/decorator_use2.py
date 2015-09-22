#!/usr/bin/env python
#-- coding: utf-8 --

import functools

#装饰函数的使用

def log(func):
	@functools.wraps(func)
	def wrapper1(*args, **kw):
		print("call func %s" %(func.__name__))
		return func(*args, **kw)
	return wrapper1

"""
@log相当于now = log(now),用functolls模块的wraps包装后 调用结束后会将now的名称置为now
"""
@log
def now():
	print("time is 2015/09/21")


now()
print(now.__name__)

def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print("%s func %s" %(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

"""
相当于now = log2("call")(now),用functolls模块的wraps包装后 调用结束后会将now的名称置为now 
"""
@log2("call")
def now2():
	print("time is 2015/09/21")


now2()
print(now2.__name__)



"""
定义一个可以传入参数或者不传参数的装饰器, @log() or @log("str")
"""

def log3(text="tarbitrary"):
	def decorator3(func):
		@functools.wraps(func)
		def wrapper3(*args, **kw):
			print("%s call func %s" %(text, func.__name__))
			return func(*args, **kw)
		return wrapper3
	return decorator3

@log3()
def now3():
	print("time is 2015/0921")


now3()
print(now3.__name__)


@log3("tuqiang")
def now4():
	print("time is 2015/0921")

now4()
print(now4.__name__)

"""
 定义一个可以传@log和@log("str")以及@log()格式的装饰器
"""
def log4(text=None):
	if text is None or isinstance(text, str):
		def decorator4(func):
			@functools.wraps(func)
			def wrapper4(*args, **kw):
				print("%s call func %s"%( text and text or "None param", func.__name__))
				return func(*args, **kw)
			return wrapper4
		return decorator4
	else:
		@functools.wraps(text)
		def wrapper4(*args, **kw):
			print("%s call func %s" %("taritrary", text.__name__))
			return text(*args, **kw)
		return wrapper4

#相当于log4(now5)
@log4
def now5():
	print("hello hello")

now5()
print(now5.__name__)

#相当于log4("tuqiang")(now5)
@log4("tuqiang")
def now6():
	print("hello tarbitrary")
now6()
print(now6.__name__)

#相当于log4()(now7)
@log4()
def now7():
	print(" hello now7")

now7()
print(now7.__name__)
