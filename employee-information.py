import mysql.connector

p1_db = mysql.connector.connect(user='root', password='', host='localhost', database='employee_information')
cursor = p1_db.cursor()

queri = "SELECT name, height, weight FROM employees"
cursor.execute(queri)

employees = []
for (name, height, weight) in cursor:
    employees.append((name, height, weight))

employees.sort(key=lambda x: (-x[1], x[2]))

for name, height, weight in employees:
    print(f"{name} {int(height)} {int(weight)}")

p1_db.close()
