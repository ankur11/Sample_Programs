#!/usr/bin/python

def scramble(a):
	return [a[i:]+a[:i] for i in range(len(a))]
print scramble('abc')
# -------------------------------------------------------------------------------------------
def scramble1(a,res=[]):
	if len(res) >=len(a):
		return
	res.append(a[1:]+a[:1])             ##       Recursion
	scramble1(res[-1])
	return res

print scramble1((1,2,3,4))
# -------------------------------------------------------------------------------------------
def per3(a, res=[]):
	for i in range(len(a)):
		offset = a[i:i+1]
		rest = a[i+1:]+a[:i]
		res.extend([offset+x for x in scramble(rest)])
	return res
print per3('1234',res=[])
# -------------------------------------------------------------------------------------------
def per(a,s=[]):
	per.c+=1
	for i in range(len(a)):
		offset = a[i:i+1]
                rest = a[i+1:]+a[:i]
		if(len(rest)<2):
			rest_list = [rest]
		else:
			rest_list = per(rest, s=[])
		for rest_per in rest_list:
			for j in range(len(rest_per)+1):
				tmp = rest_per[0:j]+offset+rest_per[j:len(rest_per)]
				if tmp not in s:
					s.append(tmp)
	return s
st = 'abcde'
per.c = 0
output = per(st)
print per.c
print "-"*60,"\n",list(output),"\nLength ",len(output)



