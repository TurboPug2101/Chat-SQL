import sqlite3

# connect to sqllite
connection=sqlite3.connect("student.db")

# create cursor object to insert record, create table
cursor=connection.cursor()

# create table
table_info="""
create table student(Name varchar(25),class varchar(25),
section varchar(25), marks int)
"""

cursor.execute(table_info)


# Insert records
cursor.execute('''Insert into student values('Ishank','Data Science','A',90)''')
cursor.execute('''Insert into student values('John',' Math','A',50)''')
cursor.execute('''Insert into student values('Harry','Data Science','B',80)''')
cursor.execute('''Insert into student values('Sniper','Data Science','A',90)''')
cursor.execute('''Insert into student values('Jacob','Math','B',70)''')
cursor.execute('''Insert into student values('Siri','Data Science','C',30)''')

print("Inserted records are")
data=cursor.execute('''Select * from student''')
# rows will be in form of list
for row in data:
    print(row)

# commit changes in db
connection.commit()
connection.close()
