import copy
from collections import defaultdict
d = {}
d[(1,2)] = 200
d[(1,4)] = 50
d[(2,3)] = 100
d[(2,4)] = 50
d[(3,4)] = 50
d[(4,5)] = 25
d[(2,5)] = 25
d[(3,5)] = 25
d[(3,6)] = 225


{(1, 2): 25, (1, 4): 75, (1, 5): 50, (1, 6): 100, (3, 6): 125, (3, 4): 50, (3, 5): 25}


print d
e = defaultdict(list)
for i,j in d:
	e[i].append(j)
#	if i in e:
#		e[i].append(j) 
#	else :
#		e[i] = [j]

print e

def optimize(d, e):
	for i in e:
		for j in e[i]:
			if(j in e):
				merge(d, e, i, j)
				print "********************************"
				print d
				print
				print e
				print "********************************"
				print
				print
				print
				return optimize(d, e)
	else :
		return (d, e)

def merge(d, e, i, j):
	arr = copy.deepcopy(e)
	for k in arr[j]:
		print i,j,k,d
		if (i,j) in d and (j,k) in d :
			if d[(i,j)] > d[(j,k)]:
				d[(i,j)] = d[(i,j)] - d[(j,k)]
				tmp = 0
				if (i,k) in d:
					tmp = d[(i,k)]
				d[(i,k)] = d[(j,k)] + tmp
				if i in e:
					e[i].append(k) if k not in e[i] else 0
				else:
					e[i] = [k]
				del d[(j,k)]
				e[j].remove(k)
				if not e[j]:
					del e[j]
			elif d[(i,j)] < d[(j,k)]:
				tmp = 0
				if (i,k) in d:
					tmp = d[(i,k)]
				d[(i,k)] = d[(i,j)] + tmp
				d[(j,k)] = d[(j,k)] - d[(i,j)]
				if i in e:
					e[i].append(k)
				else:
					e[i] = [k]
				del d[(i,j)]
				e[i].remove(j)
				if not e[i]:
					del e[i]
			elif d[(i,j)] == d[(j,k)]:
				tmp = 0
				if (i,k) in d:
					tmp = d[(i,k)]
				d[(i,k)] = d[(i,j)] + tmp
				if i in e:
					e[i].append(k)
				else:
					e[i] = [k]
				del d[(i,j)]
				del d[(j,k)]
				e[i].remove(j)
				e[j].remove(k)
				if not e[i]:
					del e[i]
				if not e[j]:
					del e[j]

print
print
print
print "-------------------------------------------"
o1, o2 = optimize(d, e)
print o1
print 
print
print o2

