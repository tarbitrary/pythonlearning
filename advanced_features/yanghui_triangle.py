#-*- coding: utf-8 -*-
#!/usr/bin/env python

def triangle(n):
	L = [1]
	while True:
		yield L
		L.append(0)
		#L = [L[i] + L[i-1] for i, v in enumerate(L)]
		L = [L[i] + L[i-1] for i in range(len(L))]
		if len(L) > n:
			break
	return "over" 

a = input("要打印杨辉三角的前几行:")
for x in triangle(int(a)):
	print(x)
