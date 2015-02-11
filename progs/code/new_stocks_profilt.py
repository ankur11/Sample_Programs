#! /usr/bin/python

def cal_profit(stock_price_list):
	max_profit = 0
	while(True):
		if not stock_price_list:
			return max_profit
		max_elm_indx = stock_price_list.index(max(stock_price_list))
		if max_elm_indx > 0:
			max_profit += (max_elm_indx)*stock_price_list[max_elm_indx] - sum(stock_price_list[:max_elm_indx])
		stock_price_list = stock_price_list[max_elm_indx+1:]

try:
	stock_prices = map(int, raw_input().split(' '))
	print cal_profit(stock_prices)
except Exception as e:
	print 'Error :', e, '\n'
