#!/usr/bin/env python
#-- coding:utf-8 --

from collections import Iterable

#����tuple
t = {1, 2, 3}
for i in t:
	print(i)

#����list
l = {'a', 'b', 'c'}
for i in l:
	print(i)

#����dict
d = {1:"tuqiang",2:"tarbitrary"}
for key in d:
	print(key)

d = {1:"tuqiang",2:"tarbitrary"}
for value in d.values():
	print(value)


d = {1:"tuqiang",2:"tarbitrary"}
for key, value in d.items():
	print(key, "->", value)


#����string
st  = "the quick brown fox jumps over the lazy dog"
for i in st:
	print(i, end="")
print()

#ʵ������java���±�ѭ��
for i, value in enumerate(l):
	print(i, value)

#�ж�һ�������Ƿ���Ե���
print(isinstance(st,Iterable))
print(isinstance(t,Iterable))
print(isinstance(l,Iterable))
print(isinstance(d,Iterable))
print(isinstance(123,Iterable))

#ͨ���ж�һ�����������Ҳ����ʵ��ͬ���Ĺ���
print(type(st))
print(type(t))
print(type(l))
print(type(d))
print(type(123))
	

