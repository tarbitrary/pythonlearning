#!/usr/bin/env python
#-*- coding:utf-8 -*-

s = set([1, 2, 3])
print(s)
print('add a value into the set', s.add(input('please innput a value')), s)
print('remove a value from the set', s.remove(input('please innput a value which you want to delete')), s)
