#!/usr/bin/env python
#-- coding: utf-8 --

import pdb
""" pdb可以调试python程序, 利用pdb -m pdb yourpythonfile.py的命令格式来进入pdb
　　调试环境, 输入l查看代码,n单步调试, p 变量名可以查看变量值, 如果不想单步调试
　　则可以引入pdb.set_trace()，程序会自动在pdb.set_trace()的位置暂停并进入pdb调
    试环境。此时可以用p查看变量，或者c继续运行(注意，进入pdb.set_trace()只需要直接python yourpythonfile.py即可.
 """

def test(n):
	s = int(n)
	pdb.set_trace()
	if s > 90:
		print("very good!")

test(input("请输入你的成绩"))
