#!/usr/bin/env python
#-- coding: utf-8 --

#一个函数加入yield就变成了一个生成器函数,每次调用生成器的next()方法时会将yield后面的字段返回,同时执行下一次next()时从yield后面开始执行

def fib(n):
	a, b, count = 0, 1, 0

	while count < n :
		yield b
		a, b = b, a + b
		count += 1
	return "done"

t = input("你想获得斐波拉契数列的前几列:")
for x in fib(int(t)):
	print(x, end=" ")
print()
