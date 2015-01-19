def a():
	print('\n\n---------------------------------\n\n')
	x=123
	def b():
		global x
		x=789
		print('\n\n---------------------------------\n\n')
		def c():
		#	nonlocal x
			x=567
			print('\n\n====',x,'=======\n\n')
		c()
	b()
	print('\n\n====',x,'=======\n\n')

a()
print('\n\n',x)
