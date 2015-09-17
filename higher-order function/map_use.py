#!/usr/bin/env python
#-*- coding: utf-8 -*-

from functools import reduce
def power(x, y=2):
	while y > 1:
		y -= 1
		x = x * x

	return  x

print(list(map(power, range(101))))
