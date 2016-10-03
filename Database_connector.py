import MySQLdb
#MySQL host: rosencrantz.berkeley.edu
#user: uspto
#password: ferrisbueller
#port: 3306
connection = MySQLdb.connect(
                host = 'rosencrantz.berkeley.edu',
                user = 'uspto',
                passwd = 'ferrisbueller')  # create the connection

cursor = connection.cursor()     # get the cursor
#cursor.execute("USE uspto") # select the database
#cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)
#cursor.execute("SELECT * FROM uspto.application Where date = '1988-06-23' and patent_id = '4920694'")
tables = cursor.fetchall() 

print tables