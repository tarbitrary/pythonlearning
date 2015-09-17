#!/usr/bin/env python
#-*- coding: utf-8 -*-

def upper2lower(st):
	if st is None:
		return None
	elif len(st) == 0:
		return ""
	elif len(st) == 1:
		return st.upper()
	else:
		return st[0].upper() + st[1:].lower()

L1 = ['tARBItrary', 'TU', 'qIANG']
L2 = map(upper2lower, L1)
print(list(L2))
