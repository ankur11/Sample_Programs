
t_cnt = int(input())
tot_cost = 0
for i in range(t_cnt):
	b_cnt, w_cnt = map(int, input().split())
	b_cost, w_cost, conv_cost = map(int, input().split())

	if b_cost > w_cost + conv_cost:
		b_cost = w_cost + conv_cost
	elif w_cost > b_cost + conv_cost:
		w_cost = b_cost + conv_cost
	tot_cost += (b_cost*b_cnt) + (w_cost*w_cnt)

print(tot_cost)
