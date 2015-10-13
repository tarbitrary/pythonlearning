#!/usr/bin/env python
#-- coding: utf-8 --

#利用getattr方法实现链式api
class Chain(object):
	def __init__(self, path = ''):
		self.path = path
	
	def __getattr__(self, attr):
		return Chain("%s/%s" % (self.path, attr))

	def __str__(self):
		return self.path

	__repr__ = __str__

c = Chain()
print(c.tarbitrary.age.view)

