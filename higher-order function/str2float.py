#!/usr/bin/env python
#-*- coding: utf-8 -*-
from functools import reduce
def mysplit(st):
	return st.split('.')

st = '123.456'
print(st, type(st))

result = reduce(lambda x, y : int(x) + int(y)*(0.1**(len(y))) , mysplit(st))
print(result, type(result))
print(reduce(lambda x, y : int(x) + int(y)*(0.1**(len(y))) , mysplit(st))) 
