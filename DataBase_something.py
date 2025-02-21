import psycopg2



connection = psycopg2.connect(database="postgres", user="postgres", password="", host="localhost", port=5432)
cursor = connection.cursor()


#cursor.execute("CREATE TABLE datacamp_courses(course_id SERIAL PRIMARY KEY,course_name VARCHAR (50) UNIQUE NOT NULL,course_instructor VARCHAR (100) NOT NULL,topic VARCHAR (20) NOT NULL)")

#cursor.execute("INSERT Into persons(personid, lastname, firstname, address, city) VALUES('1970','Godly','Stalin','Homeless_street','Moscow')")

#cursor.execute("UPDATE persons SET lastname = 'French' WHERE personid = '2763'")


cursor.execute("SELECT lastname,firstname,salary FROM persons WHERE salary != 10000 AND salary != 15000")

rows = cursor.fetchall()
for row in rows:
    print(row)


#connection.commit()
cursor.close()
connection.close()
