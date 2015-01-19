#!/usr/bin/python
def a():
  return [lambda x,i=i: i**x for i in range(0,5)]
b = a()
print b[0](2), b[4](2)
print (lambda x: (lambda i: x+i))(2)(3)
