#!/usr/bin/env python
#-*- coding:utf-8 -*-

dt = {'tarbitrary':'tuqiang', 'test':'diy'}
print(dt)
a=input('please input the key:')
b=input('please input the value:')
dt[a]=b
print(dt)
print('get the value of tarbitrary', dt['tarbitrary'])
dt['test'] = 'hello'
print(dt)
print('tarbitrary' in dt, 'tuqiang' in dt)
print('pop a value', dt.pop('tarbitrary'), dt)
print(dt.get('tq'), dt.get('tq', -1))
print('the length of dict is', len(dt))
