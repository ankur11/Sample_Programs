import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', passwd='crm#Voy0717', db='sugarcrm')
cur = db.cursor(MySQLdb.cursors.DictCursor)

#cur.execute("""select * from  IVR_payment_details""")
cur.execute("""select * from  %s """ %("IVR_payment_details",))

#rows = cur.fetchall()
#print (rows)
for row in cur.fetchall():
	print(row)
	break
