#!/usr/bin/env python
#-*- coding: utf-8 -*-

def odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

#����һ��lambda���ʽ����(��������),�����������һ������, ��������filter��
def not_divisible(n):
	return lambda x: x % n > 0

#�������������ĺ�������filter�ϻᱨ��
def not_divisible2(n, x):
	return x % n > 0

def get_prime():
	#����2,��һ������
	yield 2
	#�õ�3��ͷ��������Ȼ��
	t = odd_iter()
	while True:
		#ȡ���еĵ�һλ
		n = next(t)
		yield n
		#���˵������ܱ����е�һ��������,�õ�������
		#filter()�������ص���һ��Iterator
		t = filter(not_divisible(n), t)

for n in get_prime():
	if (n < 100):
		print(n, end=" ")
	else:
		break

