#!/usr/bin/python
def a(x):
    def b(y):
        print x**y
        b.t_n = '1235'
    return b
i = a(2)
i(5)
print i.t_n
print dir(i)

