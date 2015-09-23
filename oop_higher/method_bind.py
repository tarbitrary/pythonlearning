#!/usr/bin/env python
#-- coding: utf-8 --
import types

def set_age(self, age):
	self.age = age

class Person(object):
	pass

p1 = Person()
p2 = Person()
#给p1实例绑定set_age方法,但是这个方法在p2上面不可用
p1.setage = types.MethodType(set_age, p1)
p1.setage(50)
print(p1.age)
#p2.setage(30)

#如果要在p2上可以用则需要绑定在类上面
Person.setage = types.MethodType(set_age, Person)
p2.setage(88)
print(p2.age)

