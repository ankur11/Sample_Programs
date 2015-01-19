#!/usr/bin/python3.3
a = input()
cnt, lim = map(int, a.split())
ar = []
for i in range(cnt):
	ar.append(int(input()))
res = []
for j in range(cnt):
	for k in range(j+1, cnt):
			res.append(ar[j] ^ ar[k])
res = sorted(res)
print(res[:lim], end='')

