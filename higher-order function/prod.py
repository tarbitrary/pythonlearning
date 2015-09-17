#!/usr/bin/env python
#-*- coding: utf-8 -*-
from functools import reduce

L = list(range(1, 6))

print(reduce(lambda x, y: x*y, L))
