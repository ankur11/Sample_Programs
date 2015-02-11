import sys
import getopt

def handle_args(args):
	try:
		opts,args = getopt.getopt(args, 'hg:md', ['help', 'grammer='])
	except getopt.GetoptError:
		print '\nOlympus has fallen !!!\n\n'
		sys.exit()
	print
	print
	print opts
	print
	print args
	print
	print
#	for opt, arg in data:
#		prin

handle_args(sys.argv[1:])
