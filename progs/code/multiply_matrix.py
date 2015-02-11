#! /usr/bin/python

a = [ 
      [3,4,2]
    ]
b = 		[ [13,9,7,15], 
      		  [8,7,4,6], 
      		  [6,4,0,3] ]

c = []

print '-'*80,'\n'
tmp = 0
for i in xrange(len(a)):
	c.append([])
	for j in xrange(len(b[0])):
		for k in xrange(len(b)):
			tmp += a[i][k] * b[k][j]
		c[i].append(tmp)
		tmp = 0

print c 
print '\n','-'*80
