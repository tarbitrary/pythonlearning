#!/usr/bin/env python
#-*- coding: utf-8 -*-
l = sorted([9 , 5, 3, 2, 1,-6])
print(l)


l = sorted([9 , 5, 3, 2, 1,-6], key=abs)
print(l)

l = sorted([9 , 5, 3, 2, 1,-6], key=abs, reverse=True)
print(l)

l = sorted(['Aar', 'tu', 'Qiang', 'Z', 'a', 'count'])
print(l)

l = sorted(['Aar', 'tu', 'Qiang', 'Z', 'a', 'count'], key=str.lower)
print(l)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

#通过成绩从高到低排序
print(sorted(L, key=by_score, reverse=True))
print(sorted(L, key =  lambda x : x[1], reverse=True))

#通过名字排序
print(sorted(L, key = by_name, reverse=True))
print(sorted(L, key =  lambda x : x[0], reverse=True))
