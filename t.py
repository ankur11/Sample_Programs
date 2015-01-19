def b(a):
	len_a = len(a)
	mdiff = a[1] - a[0]
	minelm = a[0]
	for i in range(1, len_a):
		if a[i] - minelm > mdiff:
			mdiff = a[i] - minelm
		if a[i] < minelm:
			minelm = a[i]
	if (mdiff<0) :
		mdiff = -1
	return mdiff
# -----


print b([4,1,7,8,4,2,7])
