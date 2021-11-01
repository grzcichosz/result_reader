import mysql.connector
import csv

config = {
    'user': 'root',
    'password': 'example',
    'host': '127.0.0.1',
    'port': '13306',
    'database': 'flaskweb',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

add_result = ("INSERT INTO results "
               "(sample_id, date, result)"
               "VALUES (%s, %s, %s)")

with open('Data.txt') as f:
    csr = csv.reader(f, dialect="excel-tab")
    firstLine = next(csr)
    if firstLine == ['sample_id', 'date', 'result']:
        print("Wczytano")
    else:
        print("Nie wczytano")
    for line in csr:
        print(line)
        print(add_result, line)
        cursor.execute(add_result, line)

cnx.commit()
cursor.close()
cnx.close()

