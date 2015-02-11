#!/usr/bin/env python

N = 8

s = [[-1 for x in xrange(N)] for x in xrange(N)]

x_move = [2, 1, -1, -2, -2, -1, 1, 2]
y_move = [1, 2, 2, 1, -1, -2, -2, -1]


def inner_N8(x, y, cnt):
	if cnt == N*N:
		return True
	for k in xrange(8):
		x1 = x + x_move[k]
		y1 = y + y_move[k]
		if x1 < N and x1 > -1 and y1 < N and y1 > -1 and s[x1][y1] == -1:
			s[x1][y1] = cnt
			if inner_N8(x1, y1, cnt+1) == True:
				return True
			else:
				s[x1][y1] = -1
	return False 

def N8_upper():
	s[0][0] = 0
	if inner_N8(0, 0, 1) == False:
		print 'Solution does not exist'
		return False
	else:
		for i in s:
			print i
		return True

N8_upper()
