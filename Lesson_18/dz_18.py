import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='my_first_db'
)
# 1 створення нової бази
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE my_first_db')

# 2 створення в базі таблиці student
mycursor2 = mydb.cursor()
mycursor2.execute('CREATE TABLE student(id INT, name VARCHAR(255))')

# 3 створення в базі таблиці employee
mycursor3 = mydb.cursor()
mycursor3.execute('CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))')

# 4 заміна назви стовпичка в таблиці student із id на PRIMARY_KEY
mycursor4 = mydb.cursor()
mycursor4.execute('ALTER TABLE student CHANGE id PRIMARY_KEY INT ')

#5
mycursor5 = mydb.cursor()
sql = 'INSERT INTO student (PRIMARY_KEY, name) VALUES (%s, %s)'
val = [('01', 'John')]
mycursor5.executemany(sql, val)
mydb.commit()

mycursor6 = mydb.cursor()
sql2 = 'INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)'
val2 = [('01', 'John', '10000')]
mycursor6.executemany(sql2, val2)
mydb.commit()
