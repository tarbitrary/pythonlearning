#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object):
	def __init__(self, name, age):
		"""
		属性以下划线开头(不要以下划线结尾)表明是私有属性,在外部直接
		instance.propertyName是不能访问到的.
		eg:p = Person("tarbitrary", 25) p.__name错误
		但是能够通过instance._className__propertyName来访问
		eg:p._Person__name是可以访问到__name属性的,但是强烈建议你不要
		这么干，因为不同版本的Python解释器可能会把__name改成不同的变量
		名。总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠
		自觉。
		"""
		self.__name = name
		self.__age = age

	def get_personinfo(self):
		print("%s->%s"%(self.__name, self.__age))
