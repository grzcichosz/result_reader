import mysql.connector
import csv

config = {
    'user': 'root',
    'password': 'example',
    'host': '127.0.0.1',
    'port': '13306',
    'database': 'Patients',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

add_patient = ("INSERT INTO Patientsdata "
               "(name, surname, birth, pesel, sex, sampleid)"
               "VALUES (%s, %s, %s, %s, %s, %s)")

with open('Data.txt') as f:
    csr = csv.reader(f, dialect="excel-tab")
    firstLine = next(csr)
    if firstLine == ['name', 'surname', 'birth', 'pesel', 'sex', 'sampleid']:
        print("Wczytano")
    else:
        print("Nie wczytano")
    for line in csr:
        print(line)
        cursor.execute(add_patient, line)


#cursor.execute(add_employee, ('adam12', 'surname12'))

cnx.commit()

cursor.close()
cnx.close()

