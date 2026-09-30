# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bookstore')
c = con.cursor()

c.execute("""SELECT * FROM books""")

for row in c:
  print('Title: ', row[0])
  print('Author: ', row[1])
  print('Inventory: ', row[2])
c.close()