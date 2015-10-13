#!/usr/bin/env python
#-- coding: utf-8 --

class Call(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print("my name is %s" % self.name)

call = Call("tarbitrary")
call()

print(callable(call))
