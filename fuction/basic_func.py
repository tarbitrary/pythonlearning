#-*- coding:utf-8 -*-
#!/usr/bin/env python

def power2(x):
	return x*x;

def power(x, n):
	sum = x
	while n > 1:
		sum *= x
		n = n - 1
	return sum

a = input("请输入想求平方的数:")
a = int(a)
print("%d的平方是%d"%(a,power2(a)))

a = int(input("求a的b次方，请输入a:"))
b = int(input("请输入b:"))
print("%d的%d次方是%d"%(a,b,power(a,b)))
