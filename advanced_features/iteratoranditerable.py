#!/usr/bin/env python
#-- coding: utf-8 --
from collections import Iterable
from collections import Iterator

#迭代器Iterator与可迭代对象Iterable，tuple, list,dict, str都是可迭代对象但是都不是迭代器生成器既是可迭代对象也是迭代器, 简单来说可用next()方法迭代的对象就是迭代器

t = {1, 2, 3}
l = [1, 2, 3]
s = ([1, 2, 3])
d = {1:1, 2:2, 3:3}
g = (x * x for x in range(10))
r = range(100)

print("Is tuple iterable?", isinstance(t, Iterable), "Is tuple a iterator?", isinstance(t, Iterator))
print("Is list iterable?", isinstance(l, Iterable), "Is list a iterator?", isinstance(l, Iterator))
print("Is set iterable?", isinstance(s, Iterable), "Is set a iterator?", isinstance(s, Iterator))
print("Is dict iterable?", isinstance(d, Iterable), "Is dict a iterator?", isinstance(d, Iterator))
print("Is generator iterable?", isinstance(g, Iterable), "Is generator a iterator?", isinstance(g, Iterator))
print("Is range-object iterable?", isinstance(r, Iterable), "Is range-object a iterator?", isinstance(r, Iterator))

#如果要把可迭代对象Iterable转换成为迭代器对象Iterator则需要用iter()函数即可
print("用iter()函数转换后")

print("Is tuple iterable?", isinstance(iter(t), Iterable), "Is tuple a iterator?", isinstance(iter(t), Iterator))
print("Is list iterable?", isinstance(iter(l), Iterable), "Is list a iterator?", isinstance(iter(l), Iterator))
print("Is set iterable?", isinstance(iter(s), Iterable), "Is set a iterator?", isinstance(iter(s), Iterator))
print("Is dict iterable?", isinstance(iter(d), Iterable), "Is dict a iterator?", isinstance(iter(d), Iterator))
print("Is generator iterable?", isinstance(iter(g), Iterable), "Is generator a iterator?", isinstance(iter(g), Iterator))
print("Is range-object iterable?", isinstance(iter(r), Iterable), "Is range-object a iterator?", isinstance(iter(r), Iterator))

