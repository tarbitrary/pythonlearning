#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object):
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def get_personinfo(self):
		print("%s->%s"%(self.__name, self.__age))
