#!/usr/bin/env python
#-- coding: utf-8 --

import unittest


d = dict(a = 1, b = 'test')

"""
 　编写单元测试时要引入unittest，如下所示, 测试方法必须以test开头，否则不予执行
   setUp及tearDown分别在调用每一个测试方法之前和之后执行。执行单元测试有两种方式
   1: 在单元测试类里面添加, 最后执行python testfile.py
   	if __name__ == '__main__':
    		unittest.main()
   2: 直接执行python -m unittest testfile.py（推荐用法）
 
"""
class TestDict(unittest.TestCase):
	def test_init(self):
		self.assertEqual(d['a'], 1)

	def test_haha(self):
		with self.assertRaises(KeyError):
			value = d['et']

	def my_test(self):
		print("不会被执行的")
	
	def setUp(self):
		print("测试前做的事")

	def tearDown(self):
		print("测试后做的事")

if __name__ == '__main__':
	unittest.main()
