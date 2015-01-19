#!/usr/bin/python

import MySQLdb as mdb
import sys
try:
	db = mdb.connect('localhost','root','crm#Voy0717','sugarcrm')
	cur = db.cursor(mdb.cursors.DictCursor)
	dic = {'name' : 'Gupta'};
	cur.execute("select * from users where last_name =%(name)s" ,(dic))
	row = cur.fetchall()
	print(row)
except mdb.Error as e:
	print(e.args[0],e.args[1])
	sys.exit(1)
finally:
	if 'db' in locals():
		db.close()
