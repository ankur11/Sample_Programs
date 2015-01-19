#!/usr/bin/python

def a() :
	for i in range(4):
		yield i

b = a()
print next(b)
print next(b)
print next(b)
c = a()
print next(c)
print next(b)
