#!/usr/bin/env python
#--coding: utf-8 --

class Person(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "person's name is %s." %(self.name)
	
	__repr__ = __str__

p = Person("tuqiang")
p
print("*****")
print(p)
print("*****")
