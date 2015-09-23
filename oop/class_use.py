#!/usr/bin/env python
#-- coding: utf-8 --

#class定义一个类,Student类的名字,object表明这个类继承自object
class Student(object):
	#__init__自定义实例化方法,self表明对象的实例,不用传递,在调用相关方法时会自动传进去
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def get_info(self):
		print("name->%s, score->%s" %(self.name, self.score))
	
	
