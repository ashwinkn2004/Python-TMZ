import sqlite3

conn = sqlite3.connect("./Python/database/sample.db")
c = conn.cursor()

student = c.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT(
        ID INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        AGE INTEGER
    );
''')

if(student is not None):
    print("Student table created successfully")

teacher = c.execute('''
    CREATE TABLE IF NOT EXISTS TEACHER(
        ID INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        DEPARTMENT TEXT
    );
''')

if(teacher is not None):
    print("Teacher table created successfully")

# id = int(input())
# name = input()
# age = int(input())

# c.execute('''
#     INSERT INTO STUDENT (id, name, age)
#     VALUES (?, ?, ?);
# ''', (id, name, age))


# conn.commit()


c.execute("select * from student")

for i in c.fetchall():
    for j in i :
        print(j, end = " ")
    print()
print("\n")

# UPDATE
c.execute('''
    UPDATE STUDENT SET age = 22 where name = 'ASHWIN';
''')

c.execute("select * from student")

for i in c.fetchall():
    for j in i :
        print(j, end = " ")
    print()
print("\n")

# DELETE

id = int(input("Enter id : "))

c.execute('''
    DELETE FROM STUDENT WHERE id = ?;
''', (id, ))

c.execute("select * from student")

for i in c.fetchall():
    for j in i :
        print(j, end = " ")
    print()
print("\n")

conn.commit()