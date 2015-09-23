#!/usr/bin/env python
#-- coding: utf-8 --

class Animal(object):
	def run(self):
		print("animals is running")

class Dog(Animal):
	#dog有定义自己的run方法因此调用它的run方法时会调用自己的run方法
	def run(self):
		print("dog is running")


class Cat(Animal):
	#cat没有定义自己的run方法,在调用它的run方法时默认使用父类的run方法
	#当类或方法没有实体时用pass表示结束
	pass

class Tortoise(object):
	"""虽然没有继承自animal但是在任何要调用run方法的地方我都可以替换animal及其子类, 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
	"""
	def run(self):
		print("even if i am not extends from animal, but i can run slowly")

