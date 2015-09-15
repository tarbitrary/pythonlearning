#!/usr/bin/env python
#-- coding: utf-8 --

g = (x * x for x in list(range(10)))

for x in g:
	print(x)
print("*********************************")
	
g = (x * x for x in list(range(10)))
while True:
	print(next(g))

