# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bookstore')
c = con.cursor()

param1 = 50
param2 = 'Throne of Glass'
sql = "UPDATE `books` SET `Inventory`=" +str(param1) + " WHERE TItle = '" + param2 + "' "
c.execute(sql)

con.commit()
c.close()