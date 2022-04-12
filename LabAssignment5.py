import sqlite3
from sqlite3 import Error

print('This is the Beginning of the database application.\n')

# create a connection
try:
    print('Connecting to database file LabAssignment5.sqlite')
    conn = sqlite3.connect('LabAssignment5.sqlite')
    print('Connected.\n')
except Error as e:
    print(e)


# create a cursor
try:
    print('Creating a cursor.')
    c = conn.cursor()
    print('Cursor created.\n')
except Error as e:
    print(e)

# Create the STUDENT table
try:
    print('Creating table.\n')
    c.execute("""CREATE TABLE STUDENT (
        studentId           integer PRIMARY KEY,
        studentLastName     text    NOT NULL,
        studentFirstName    text    NOT NULL,
        dateOfBirth         text    NOT NULL,
        isActive            text    NOT NULL
        )""")
    print('Table created.\n')
except Error as e:
    print(e)


# Input the table data
try:
    print('Defining our table input data.\n')
    manyStudents = [
        (100001,	'Johnson',	'Ariel',    '1999-07-10',	'N'),
        (100002,	'Green',	'Robin',	'2001-11-02',	'N'),
        (100003,	'Johnson',	'Charles',	'1995-01-12',	'N'),
        (100004,	'Pearson',	'Jeffery',	'1996-02-0',	'N'),
        (100005,	'Sears',	'Miguel',	'1998-10-31',	'N'),
        (100006,	'Kyle',	    'Leah',	    '2000-05-29',	'N'),
        (100007,	'Myers',	'Lynda',	'1980-08-24',	'N')
    ]
    print('Table input data defned.\n')
except Error as e:
    print(e)

try:
    print('Inserting new rows.\n')
    c.executemany("INSERT INTO STUDENT VALUES (?,?,?,?,?)", manyStudents)
    conn.commit()
    print('New rows are inserted. Current rows in the table are:')
except Error as e:
    print(e)


# Display the STUDENT table data
try:
    c.execute("SELECT * FROM STUDENT")
    items = c.fetchall()
    for item in items:
        print(item)
    print('======================================\n')
except Error as e:
    print(e)

# Delete students with studentId's 100002, 100005, 100006.
try:
    c.execute(
        "DELETE FROM STUDENT WHERE studentId == 100002 OR studentId == 100005 OR studentId == 100006")
    conn.commit()
    print('Rows are deleted. Current rows in the table are:')
except Error as e:
    print(e)

# Display the new STUDENT table data
try:
    c.execute("SELECT * FROM STUDENT")
    items = c.fetchall()
    for item in items:
        print(item)
    print('======================================\n')
except Error as e:
    print(e)


try:
    c.execute("""UPDATE STUDENT SET studentLastName = 'Lee'
           WHERE studentId = 100007
      """)
    conn.commit()
    print('Last name is updated. The updated row is:')
    c.execute("SELECT * FROM STUDENT WHERE studentId = 100007")
    items = c.fetchall()
    for item in items:
        print(item)
    print('======================================\n')
except Error as e:
    print(e)


# Take user input to see student information
try:
    userInputStudent = int(
        input("Which student’s information do you want to see?"))
    c.execute("SELECT * FROM STUDENT WHERE studentId = (?)",
              (userInputStudent,))
    items = c.fetchall()
    for item in items:
        print(item)
    print('======================================\n')
except Error as e:
    print(e)

try:
    while True:
        userInputContinue = input("Do you want to see another student(Y/N)?")
        if userInputContinue == "Y":
            userInputStudent = int(
                input("Which student’s information do you want to see?"))
            c.execute("SELECT * FROM STUDENT WHERE studentId = (?)",
                      (userInputStudent,))
            items = c.fetchall()
            for item in items:
                print(item)
            print('======================================\n')
        elif userInputContinue == "N":
            c.execute("DELETE FROM STUDENT")
            print('All data in the table is deleted.\n')
            print('Program terminated.')
            break
        else:
            print("Please enter a valid command.")
except Error as e:
    print(e)

# Delete table
try:
    c.execute("DROP TABLE STUDENT")
    print('Table deleted.')
except Error as e:
    print(e)

conn.commit()
conn.close()
