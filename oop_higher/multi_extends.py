#!/usr/bin/env python
#-- coding: utf-8 --
#多重继承

class Animal(object):
	pass

class Runnable(Animal):
	pass

class Flyable(Animal):
	pass

class Tortoise(Runnable):
	pass

class Dark(Flyable, Runnable):
	pass

t = Tortoise()
d = Dark()

print(isinstance(t, Animal))
print(isinstance(d, Animal))
print(isinstance(t, Runnable))
print(isinstance(d, Runnable))
print(isinstance(d, Flyable))
print(isinstance(t, Flyable))
