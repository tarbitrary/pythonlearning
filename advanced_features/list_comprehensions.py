#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

L = list(range(100))
print(L)

l = [i*i for i in L]
print(l)

lt = [L[i]+L[i-1] for i in L]
print(lt)

#同时遍历两个字符串
lt = [ a + b for a in "tuquiang" for b in "tarbitrary"]
print(lt)

#列出当前文件夹下面的所有文件和目录
lt = [d for d in os.listdir(".")]
print(lt)

d = {"a":"b", "c":"d", "e":"f"}
result = [key + '=' + value for key, value in d.items()]
print(result)

#将里面的所有字符串转换成小写
L = ['Hello', 'World', 18, 'Apple', None]
k = [st.lower() for st in L if isinstance(st, str)]
print(k)
