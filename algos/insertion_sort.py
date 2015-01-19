#! /usr/bin/python
from __future__ import print_function
import time
#input_str = raw_input('Enter the list - ')
#a = [int(x) for x in input_str.split() if x.isdigit()]
a = [5,4,6,3,8, 56,8,3,0,2,6,23,8,34,67,89,3,23,5,78,5,234,457,62,55]*1000
start = time.clock()
for i in range(1,len(a)):
	for j in range(i, 0, -1):
		if a[j] < a[j-1]:
			(a[j], a[j-1]) = (a[j-1], a[j])
print('First algo time - ',time.clock() - start,"\n\n")
#print(a)


#**************************************************************************************************


a = [5,4,6,3,8, 56,8,3,0,2,6,23,8,34,67,89,3,23,5,78,5,234,457,62,55]*1000
start = time.clock()
for i in range(1,len(a)):
	key = a[i]
	for j in range(i-1, -2, -1):
		if key < a[j] and j>=0:
			a[j+1] = a[j]
		else:
			a[j+1] = key
			break;
print('Second algo time - ',time.clock() - start,"\n\n")
#print(a)
#
#
#
##**************************************************************************************************
#
#
##input_str = raw_input('Enter the list - ')
##a = [int(x) for x in input_str.split() if x.isdigit()]
##a = [2,4,5,6,3]
a = [5,4,6,3,8, 56,8,3,0,2,6,23,8,34,67,89,3,23,5,78,5,234,457,62,55]*1000
start = time.clock()
for i in range(1,len(a)):
	key = a[i]
	k = i
	for j in range(i-1, -1, -1):
		if key < a[j]:
			a[j+1] = a[j]
			k = j
	a[k] = key
print('Third algo time - ',time.clock() - start,"\n\n")
#print(a)
#
#
##**************************************************************************************************
#
#
a = [5,4,6,3,8, 56,8,3,0,2,6,23,8,34,67,89,3,23,5,78,5,234,457,62,55]*1000
start = time.clock()
for i in range(1,len(a)):
	key = a[i]
	j = i-1
	while(j >= 0 and key < a[j]):
		a[j+1] = a[j]
		j = j-1
	a[j+1] = key
print('Fourth algo time - ',time.clock() - start,"\n\n")
#print(a)
