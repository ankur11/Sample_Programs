# http://www.codechef.com/problems/SUMSLOPE

n = int(raw_input())
l = []
for _ in xrange(n):
	a,b = map(int, raw_input().split(' '))
	l.append((a,b))
for a,b in l:
	cnt = 0
	for i in xrange(a, b+1):
		i = str(i)
		for j in xrange(1, len(i)-1):
#			if ( ( int(i[j]) > int(i[j-1]) and int(i[j]) > int(i[j+1])) or ( int(i[j]) < int(i[j-1]) and int(i[j]) < int(i[j+1])) ):
			if ( ( i[j] > i[j-1] and i[j] > i[j+1]) or ( i[j] < i[j-1] and i[j] < i[j+1]) ):
				cnt += 1
	print cnt
