#!/usr/bin/evn python
#-- coding: utf-8 --
from io import BytesIO

b = BytesIO()
b.write("涂强".encode("utf-8"))
print(b.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
