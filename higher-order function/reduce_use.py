#!/usr/bin/env python
#-*- coding: utf-8 -*-

from functools import reduce
def add(x, y):
	return x + y

print(reduce(add,[int(x) for x in range(101)]))
