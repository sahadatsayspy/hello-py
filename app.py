from mysql import connector

db = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_database"
)

mycursor = db.cursor()

# Make new Database command.
#mycursor.execute("CREATE DATABASE py_database")

# Make new table
'''
mycursor.execute(
    "CREATE TABLE person (name VARCHAR(50), age smallint UNSIGNED, person_id int PRIMARY KEY AUTO_INCREMENT)")
'''
# Describe a table. how to design
'''
mycursor.execute("DESCRIBE person")
for x in mycursor:
    print(x)
'''

# insert data to database table
'''
mycursor.execute("INSERT INTO person (name, age) VALUES (%s, %s)",
                 ("Md Hasan", 32))
db.commit()
'''
# Select query
'''
mycursor.execute("SELECT * FROM person")
for x in mycursor:
    print(x)
'''
# Add new column in the table
#mycursor.execute("ALTER TABLE person ADD COLUMN food VARCHAR(50) NOT NULL")
'''
mycursor.execute("DESCRIBE person")
for x in mycursor:
    print(x)
'''
# DROP a column name
'''
mycursor.execute("ALTER TABLE person DROP food")
mycursor.execute("DESCRIBE person")
for x in mycursor:
    print(x)
'''
# CHANGE column name
'''
mycursor.execute("ALTER TABLE person CHANGE name first_name VARCHAR(40)")
mycursor.execute("DESCRIBE person")
for x in mycursor:
    print(x)
'''
