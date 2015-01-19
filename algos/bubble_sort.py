#! /usr/bin/env python

A = [3,1,4,2,7,90,3,5,768,12,45,879,65,123,456,7,890,457,234,436,76,88,0]
A = [9,8,7,6,5,4,3,2,1,0]
indx = -1
while indx <= len(A)-3:
	for i in range(len(A)-1, indx, -1):
		if(A[i] < A[i-1]):
			(A[i], A[i-1]) = (A[i-1], A[i])
	indx += 1
	print(A)

#print(A)

