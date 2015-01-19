#! /usr/bin/env python

cnt_stu, cnt_spell = map(int, raw_input().split(' '))
spell_list = []
for i in xrange(cnt_stu):
	spell_list.append(raw_input())

stats_data = {}
max_spell_count = 0
for j in xrange(1, len(spell_list)):
	for k in xrange(j+1, len(spell_list)+1):
		stats_data[(j,k)] = 0
		for l in xrange(cnt_spell):
			if spell_list[j-1][l] == '1' or spell_list[k-1][l] == '1':
				stats_data[(j,k)] += 1
		max_spell_count = stats_data[(j,j+1)] if stats_data[(j,j+1)] > max_spell_count else max_spell_count

print max_spell_count
print len([x for x in stats_data if stats_data[x] == max_spell_count])
