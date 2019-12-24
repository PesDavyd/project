
import mysql.connector
import csv
mydb = mysql.connector.connect(
host="localhost",
user="root" ,
passwd="School2009"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS db1")
mycursor.execute("use db1")
mycursor.execute("""CREATE TABLE IF NOT EXISTS films(
   id INTEGER PRIMARY KEY,
   film_name TEXT,
   year INTEGER,
   rate TEXT,
   budget BIGINT,
   cash_collection BIGINT,
   country VARCHAR(15),
   genre TEXT,
   director TEXT,
   producer TEXT);
   """)
filename = "films.csv"
with open(filename, 'r', newline = '') as file:
   reader = csv.reader(file)
   for row in reader:
       mycursor.execute("""
           INSERT INTO films(id, film_name, year, rate, budget, cash_collection, country, genre, director, producer)
           VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
       """
       %(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
       )
       mydb.commit()
