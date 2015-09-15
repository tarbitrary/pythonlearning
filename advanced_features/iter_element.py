#!/usr/bin/env python
#-- coding:utf-8 --

from collections import Iterable

#迭代tuple
t = {1, 2, 3}
for i in t:
	print(i)

#迭代list
l = {'a', 'b', 'c'}
for i in l:
	print(i)

#迭代dict
d = {1:"tuqiang",2:"tarbitrary"}
for key in d:
	print(key)

d = {1:"tuqiang",2:"tarbitrary"}
for value in d.values():
	print(value)


d = {1:"tuqiang",2:"tarbitrary"}
for key, value in d.items():
	print(key, "->", value)


#迭代string
st  = "the quick brown fox jumps over the lazy dog"
for i in st:
	print(i, end="")
print()

#实现类似java的下标循环
for i, value in enumerate(l):
	print(i, value)

#判断一个对象是否可以迭代
print(isinstance(st,Iterable))
print(isinstance(t,Iterable))
print(isinstance(l,Iterable))
print(isinstance(d,Iterable))
print(isinstance(123,Iterable))

#通过判断一个对象的类型也可以实现同样的功能
print(type(st))
print(type(t))
print(type(l))
print(type(d))
print(type(123))
	

