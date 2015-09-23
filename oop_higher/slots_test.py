#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object): 
	#使用slots方法限制person实例只能绑定name与age属性，避免动态方法可以随意给实例绑定属性的问题
	__slots__=('name', 'age')

p = Person()
p.name = "tarbitrary"
p.age = 40
print(p.name , p.age)
p.test=34

