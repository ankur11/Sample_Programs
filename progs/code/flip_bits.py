

#a = 5
#101
#1, 2,
#0, 1
#1, 0
import sys
def flip_bits(n):
	pass

def flipped_bin2dec(n):
	res = 0
	res = reduce(lambda x,y: x + y, [ ((int(n[i])+1)%2)*pow(2,31-i) for i in range(0, len(list(n))) ])
	return res

def dec2bin(n):
	bin_str = ''
	if n == 0 :
		return '0'*32
	while n >= 1:
		bin_str = str(n % 2) + bin_str
		n = n/2
#		print n, n%2
#		print
	return '0'*(32-len(bin_str)) + bin_str


elm = 67108864
#elm = 11
s = dec2bin(elm)
print s
print (flipped_bin2dec(s))
sys.exit()
n = int(input())
l = []
for i in range(n):
	l.append(int(input()))
for elm in l:
	s = dec2bin(elm)
	print (flipped_bin2dec(s))
