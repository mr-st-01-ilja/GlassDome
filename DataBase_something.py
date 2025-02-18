import psycopg2



connection = psycopg2.connect(database="postgres", user="postgres", password="", host="localhost", port=5432)

cursor = connection.cursor()



#cursor.execute("INSERT Into persons(personid, lastname, firstname, address, city) VALUES('1970','Godly','Stalin','Homeless_street','Moscow')");

#cursor.execute("UPDATE persons SET lastname = 'French' WHERE personid = '2763';")
#cursor.execute("UPDATE persons SET firstname = 'Baguette' WHERE personid = '2763';")
#cursor.execute("UPDATE persons SET address = 'Tower_street' WHERE personid = '2763';")
#cursor.execute("UPDATE persons SET city = 'France' WHERE personid = '2763';")

cursor.execute('SELECT * FROM persons ORDER BY personid')
rows = cursor.fetchall()
for row in rows:
    print(row)


connection.commit()
connection.close()

#cursor.execute("SELECT * from persons.;")
# record = cursor.fetchall()

#print("Data from Database:- ", record)


