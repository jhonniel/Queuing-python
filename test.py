import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="shark",database="pharmacy")

mycursor=mydb.cursor()

mycursor.execute("select * from customer")

for i in mycursor:
	print(i)
