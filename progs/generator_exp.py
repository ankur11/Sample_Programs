#!/usr/bin/python

def a():
	return (i for i in range(8))

b = a()
print next(b)
print next(b)
print next(b)
c = a()
print next(c)
print next(b)

print
print
print

d = (i for i in range(8))
print next(d)
print next(d)
print next(d)
