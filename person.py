#!/usr/bin/python
from __future__ import print_function
from classtools import AttrDisplay
class Person(AttrDisplay):
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1+percent))
#	def __repr__(self):
#		return '[Person %s, %s]' %(self.name, self.pay)

class Manager(Person):
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
	print(Person('Hello Ankurrrrrr').lastName(),'\n\n')


	bob = Person('Bob Smith')
#	sue = Person('Sue Jones',job='dev',pay=100000)
	sue = Person('Sue Jones',job='dev',pay=100000)
	print(bob.name,bob.pay);
	print(sue.name,sue.pay)
	print(sue.lastName())
	sue.giveRaise(.10)
	print(sue.pay)
	print(sue)
	tom = Manager('Tom Jones', 'mgr', 50000);
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)
