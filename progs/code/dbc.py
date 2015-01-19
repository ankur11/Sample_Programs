import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='crm#Voy0717', db='sugarcrm')
cur = db.cursor()

cur.execute("""select * from  %s """ %("IVR_payment_details"))

for row in cur.fetchall():
	print row

