#! /usr/bin/python

class A_Class:
	def imethod(self, x):
		print([self, x])

	@staticmethod
	def smethod(x):
		print "Simply printing",x


	@classmethod
	def cmethod(cl_ins, x):
		print([cl_ins, x])

	@property
	def prop_method(x):
		print([x])

a = A_Class()
a.imethod(2)
print
print
print
a.smethod(3)
print
print
print
a.cmethod(4)
print
print
print
a.prop_method
