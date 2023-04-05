import mysql.connector as msql
from mysql.connector import Error
import csv 


conn = msql.connect(--connection_string_here--)

csv_data = csv.reader(open('csvv.csv'))
next(csv_data)
cursor=conn.cursor()
for row in csv_data:
    cursor.execute('INSERT INTO Linux.Cp(pid,name,last) VALUES(%s,%s, %s)',row)


conn.commit()
print("Total number of rows in table: ", cursor.rowcount)
print(cursor.rowcount, "record inserted.")

result = cursor.fetchall()
for row in result:
    print(row)
    print("\n")
cursor.close()