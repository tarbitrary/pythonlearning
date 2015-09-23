#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object):
	"""propert装饰器能够把一个方法调用变成属性的形式，原来需要写p = Person()
	   p.get_score()现在只用写p.get_score
	"""
	@property
	def get_score(self):
		return self._score

	"""定义set方法(此处.setter前面的必须与@property修饰的方法名相同) p.set_score=20 等价于原来的p.set_score(20)"""
	@get_score.setter
	def set_score(self, value):
		self._score = value
	#推荐用法,get, set方法定义成一样的，类似于可读写属性
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value
	#只定义一个get方法的话，就是只读属性
	@property	
	def fullname(self):
		return self.name + "@gmail.com"
	



p = Person()
p.set_score = 80
print(p.get_score)
p.name = "tarbitrary"
print(p.name)
print(p.fullname)
