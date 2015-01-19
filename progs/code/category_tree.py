#! /usr/bin/env python

def readable_cat_tree(d, indent=0):
	for key, value in d.iteritems():
		print '\t' * indent + str(key)
		if isinstance(value, dict):
			readable_cat_tree(value, indent+1)
		else:
			print '\t' * (indent+1) + str(value)

cat_tree = {'Home':{}}
for line in open(r'tree.csv'):
	obj = cat_tree['Home']
	line = line.strip('\n')
	arr = line.split('|')
	for elm in arr:
		if elm not in obj:
			obj[elm] = {}
		obj = obj[elm]
print '-'*80
readable_cat_tree(cat_tree)
print '-'*80
		
