#!/usr/bin/env python
#-*- coding: utf-8 -*-

def odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

#返回一个lambda表达式函数(匿名函数),这个函数接受一个参数, 可以用在filter上
def not_divisible(n):
	return lambda x: x % n > 0

#接受两个参数的函数用在filter上会报错
def not_divisible2(n, x):
	return x % n > 0

def get_prime():
	#返回2,第一个素数
	yield 2
	#得到3开头的所有自然数
	t = odd_iter()
	while True:
		#取序列的第一位
		n = next(t)
		yield n
		#过滤掉所有能被序列第一次整除的,得到新序列
		#filter()函数返回的是一个Iterator
		t = filter(not_divisible(n), t)

for n in get_prime():
	if (n < 100):
		print(n, end=" ")
	else:
		break

