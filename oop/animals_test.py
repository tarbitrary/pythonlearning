#!/usr/bin/env python
#-- coding: utf-8 --
import types
import animals

p = animals.Animal()
dog = animals.Dog()
cat = animals.Cat()
tortoise = animals.Tortoise()

p.run()
dog.run()
cat.run()
tortoise.run()

print("p->", type(p), isinstance(p, animals.Animal))
print("dog->", type(dog), isinstance(dog, animals.Animal))
print("cat->", type(cat), isinstance(cat, animals.Animal))
print("tortoise->", type(tortoise), isinstance(tortoise, animals.Animal))

#判断一个对象是否为函数的,可以用types.FunctionType
def fn():
	psss

print(type(fn)==types.FunctionType)



#获取一个对象所有的属性和方法dir
print("str's methods and properties", dir("tarbitrary"))
print("Animals's methods and properties", dir(p))

"""getattr(obj, property)取得对象的某个属性，没有抛出异常、setattr(obj, property,value)为对象设置某个属性,以及hasattr(obj, property)判断对象是否有某个属性"""
class attrtest(object):
	def __init__(self, x, y):
		self.x = x
		self.__y = y

	def getinfo(self):
		print(self.x, self.__y)
		
at = attrtest(2,3)
print(getattr(at, "x"))
at.getinfo()
print("has attr __y?", hasattr(at, "__y"))
print("has attr _attrtest__y?", hasattr(at, "_attrtest__y"))
print(setattr(at, "__y", 5))
print("has attr __y?", hasattr(at, "__y"))
at.getinfo()
#私有成员变量要通过这种方法来设置，
print(setattr(at, "_attrtest__y", 6))
at.getinfo()
print(getattr(at, "__y"))
