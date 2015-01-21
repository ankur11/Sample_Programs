#! /usr/bin/python

def cal_profit(stock_price_list, existing_stock_list, amnt):
	if not stock_price_list:
		return amnt
	else:
		buy_amnt = amnt - stock_price_list[0]
		bought_stocks = existing_stock_list[:]
		bought_stocks.append(stock_price_list[0])
		sell_amnt = amnt + len(existing_stock_list)*stock_price_list[0]
		sell_and_buy_amnt = sell_amnt - stock_price_list[0]
		return max(
			cal_profit( stock_price_list[1:], bought_stocks, buy_amnt ),
			cal_profit( stock_price_list[1:], [], sell_amnt ),
			cal_profit( stock_price_list[1:], [stock_price_list[0]], sell_and_buy_amnt ),
			cal_profit( stock_price_list[1:], existing_stock_list, amnt )
		)

try:
	stock_prices = map(int, raw_input().split(' '))
	print cal_profit(stock_prices[:], [], 0)
except Exception as e:
	print 'Error :', e, '\n'









#
#l = [1,2,50,49]
#l = [5, 3, 2]
#l = [5,3,2,5]
#
#def cal_profit(actn, l, s_l, amnt):
#	print actn
#	if not l:
#		print '\n', 'returned amount ---------', amnt, '\n'
#		return amnt
#		
#	else:
#		buy_amnt = amnt - l[0]
#		bought_stocks = s_l[:]
#		bought_stocks.append(l[0])
#		sell_amnt = amnt + len(s_l)*l[0]
#		sold_stocks = []
#		both_amnt = sell_amnt - l[0]
#		both_stocks = [l[0]]
#		hold_amnt = amnt
#		return max(
#			cal_profit('buyy', l[1:], bought_stocks, buy_amnt),
#			cal_profit('sell', l[1:], sold_stocks, sell_amnt),
#			cal_profit('both', l[1:], both_stocks, both_amnt),
#			cal_profit('hold', l[1:], s_l, amnt)
#		)
#
#
#print cal_profit('init', l[:], [], 0)
