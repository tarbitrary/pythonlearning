#!/usr/bin/env python
#-- coding: utf-8 --

"""
	如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个
	__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断
	调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration
	错误时退出循环。
"""

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.b + self.a
		if self.a > 1000:
			raise StopIteration()
		return self.a

	"""
	   如果要实现类似list的切片或者利用下标访问的功能则要实现__getitem__方法
	"""

	def __getitem__(self, n):
		#如果是下标访问则直接返回第n个值即可
		if (isinstance(n, int)):
			self.a , self.b = 1, 1
			for x in range(n):
				self.a, self.b = self.b, self.a + self.b
			return self.a

		#如果是切片的话则要判断一下
		if (isinstance(n, slice)):
			self.a, self.b = 0, 1
			x = n.start
			y = n.stop
			L = []
			if x is None:
				x = 0
			for i in range(y):
				self.a, self.b = self.b, self.a + self.b
				if i >= x:
					L.append(self.a)
			return L


fib = Fib()
for x in fib:
	print(x, end=', ')


f = Fib()
print("f[0]->", f[0])
print("f[1]->", f[1])
print("f[10]->", f[10])

print("f[0:0]->", f[0:0])
print("f[0:3]->", f[0:3])
print("f[0:1]->", f[0:1])
print("f[0:5]->", f[0:5])
print("f[3:5]->", f[3:5])
