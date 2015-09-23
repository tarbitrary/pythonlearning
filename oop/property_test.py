#!/usr/bin/env python
#-- coding: utf-8 --
class Person:
	#这样定义的name是类的属性
	name = "tarbitrary"


p = Person()
#打印实例的name属性，因为实例没有name属性所以查找类的name属性
print(p.name)
#打印类的name属性
print(Person.name)
#给实例绑定name属性
setattr(p, "name", "tuqiang")
#实例的name属性
print(p.name)
#类的name属性
print(Person.name)
del p.name
print(p.name)
"""在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性"""
