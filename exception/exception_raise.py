#!/usr/bin/env python
#-- coding: utf-8 -- 
class ZeroError(ValueError):
	pass

try:
	print("I want to throw a exception which was defined by myself")
	raise ZeroError("zero error")
except ValueError as e:
	print("catch e ", e)
except BaseException as e:
	print("catch baseexception e", e)
finally:
	print("haha the end")


print("everything is over")
