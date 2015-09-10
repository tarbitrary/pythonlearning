#!/usr/bin/env python
#-*- coding:utf-8 -*-
a = [1, 2, 3,5, 8]
print(a)
a.append(9)
print(a)
print(a[0])
print('index use:', a.index(5))
print('count use:', a.count(8))
a.append(8)
print('count use:', a.count(8))
print('befor insert', a)
a.insert(1, 4)
print('after insert', a)
a.pop()
print('pop a value out of the list', a)
a.pop(0)
print('pop the certain position value', a)
print('get the last value of the list', a[-1], a[len(a)-1])
