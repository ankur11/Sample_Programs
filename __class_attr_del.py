#!/usr/bin/env python

class Parent_Class:
	def hello(self):
		print "Hello World";

class Child_Class(Parent_Class):
	def hello(self):
		print 'Damn!!!!!!!!!!!!!!!!!!!!!!!!!!!!!';

Child_Class().hello()	
a = Child_Class()
a.hello()
a.__class__.__bases__[0]().hello()
del a.__class__.__bases__[0].hello
a.hello()
b = Child_Class()
b.hello()
