#!/usr/bin/python
def a(N):
	return [lambda : x**2 for x in range(N)]
for i in a(5):
	print i()
print "-----------------------------------------"
def b(N):
	for i in range(N):
		yield i**2
for j in b(5):
	print(j)
print "------------------------------------------"
def c(N):
	return [lambda x=x: x**2 for x in range(N)]
for i in c(5):
	print i()
