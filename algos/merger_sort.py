#!/usr/bin/env python
from __future__ import print_function
import math, sys
#a = [1,3,6,9,11,13,14]
#b = [2,4,5,7,8,10,12]
#c = []
#a_indx = 0
#b_indx = 0
##for i in range(len(a)+len(b)):
#while(a_indx < len(a) and b_indx < len(b)):
#	if a[a_indx] > b[b_indx]:
#		c.append(b[b_indx])
#		b_indx += 1
#	else:
#		c.append(a[a_indx])
#		a_indx += 1
#c.extend(a[a_indx:])
#c.extend(b[b_indx:])
#
#print(c)
#

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#
#a = [1,3,6,9,11,13,14]
#b = [2,4,5,7,8,10,12]
#c = []
#a_indx = 0
#b_indx = 0
#while(a_indx < len(a) and b_indx < len(b)):
#	if a[a_indx] > b[b_indx]:
#		c.append(b[b_indx])
#		b_indx += 1
#	else:
#		c.append(a[a_indx])
#		a_indx += 1
#
#if a_indx >= len(a):
#	c.extend(b[b_indx:])
#elif b_indx >= len(b):
#	c.extend(a[a_indx:])
#
#print(c)
#

def merge(A, p, q, r):
	B = A[p:q]
	C = A[q:r]
	print('\tMerger - ',A[p:r], ' P = ',p, ' Q = ',q,' R = ',r,' B = ',B,' C = ',C,end='  ')
	B_indx = 0
	C_indx = 0
	B.append(9999999999)
	C.append(9999999999)
	for i in range(p,r):
		if B[B_indx] > C[C_indx]:
			A[i] = C[C_indx]
			C_indx += 1
		else:
			A[i] = B[B_indx]
			B_indx += 1
	print('Returned Array - ',A[p:r],'\n')


def mergeSort(A, p, r):
	print ('Merger Sort Called ',A[p:r], ' P = ',p,' R = ',r,' ')
	if(p < r-1):
		q = int(math.floor((p+r)/2))
		print ('\t\t\t\t\t\t\tQ = ',q)
		mergeSort(A,p,q)
		mergeSort(A,q,r)
		merge(A,p,q,r)
	else:
		print('\t\tTermination at - ',A[p:r],' P = ',p,' R = ',r,' ')

A = [5,7,3,1,9]
print(A)
mergeSort(A, 0, len(A))
print ('\nFinal Array = ',A)

#A = [1,3,6,9,11,13,14,    2,4,5,7,8,10,12,15,15,16]	
#A = [5,2]
#A = [2, 4, 5, 3, 8, 1]
#  in  [8, 1]  P =  4  Q =  5  R =  6	
#merge(A, 4, 5, 6)
#merge(A, 0, int(math.floor((0+len(A))/2)), len(A))
#print (A)
#sys.exit()
#
