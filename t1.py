n = raw_input()
a,b = map(int, n.split())
#a = int(a)
#b = int(b)
print a,b
n = raw_input()
arr = map(int, n.split())
print arr
h = set(arr)
print h
r = 0
for elm in arr:
	if elm-b in h:
		r += 1
print r
