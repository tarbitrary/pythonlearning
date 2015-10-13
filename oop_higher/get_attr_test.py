#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object):
	def __init__(self, name):
		self.name = name

	#自定义获取类的属性的方法
	def __getattr__(self, attr):
		if attr == "age":
			return lambda:25
		elif attr == "email":
			return "tarbitary@gmail.com"
		elif attr== "name":
			return self.name
		else:
			raise AttributeError("Person has no attribute named %s"  %(attr))

p = Person("tarbitrary")
print(p.name)
print(p.age)
print(p.age())
print(p.email)
print(p.tel)
