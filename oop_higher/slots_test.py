#!/usr/bin/env python
#-- coding: utf-8 --

class Person(object): 
	#ʹ��slots��������personʵ��ֻ�ܰ�name��age���ԣ����⶯̬�������������ʵ�������Ե�����
	__slots__=('name', 'age')

p = Person()
p.name = "tarbitrary"
p.age = 40
print(p.name , p.age)
p.test=34

