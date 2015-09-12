#!/usr/bin/env python
#-*- encoding:utf-8 -*-
L = list(range(100))

print("init list:", L)

#取第一到第十个数
#切片用法L[a:b:c] a起始位置(不写默认为0),b结束位置(不写默认为len(L)),c步长(不写默认为1), 区间为左闭右开区间[a,b),即包含a,不包含b, 如果b不写的时候最后一个字符是包含的
print(L[0:])
print(L[0:10])
print(L[:10])
print(L[0:])
print(L[0:100])
#如果b超出下标范围,不论超出多少都只包含到最后一个
print(L[0:101])
print(L[0:-1])
print(L[:10:2])
print(len(L))

#最后一个元素的位置可以用-1来表示
print(L[-1:-2:-1])
print(L[-2:])
print(L[-2:-1])


