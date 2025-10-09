# Working with Databases in Python 🐍

Databases are essential for storing, managing, and retrieving data efficiently.  
Python provides various ways to work with both **SQL** and **NoSQL** databases.

---

## 1️⃣ Accessing MySQL or MariaDB via Console

You can connect to MySQL or MariaDB directly from your terminal.

**Common Paths:**

C:\Program Files\MySQL\MySQL Server 8.0\bin

C:\Program Files\MariaDB 10.11\bin


**Basic Commands:**
```bash
mysql -u root -p
mysql -V
mysql -h localhost -u root -p
```
To change the drive in console:
F:

## 2️⃣ Basic MySQL / MariaDB Commands
```Python
CREATE DATABASE learn;
SHOW DATABASES;
USE learn;

CREATE TABLE people (
    name VARCHAR(20),
    age INT,
    sex CHAR(1)
);

INSERT INTO people VALUES ('Alireza', 33, 'M');
SELECT * FROM people;
SELECT name FROM people WHERE sex = 'F';
DESC people;
SHOW TABLES;
```
### ✅ Tip:
Use uppercase for SQL commands (e.g., CREATE, INSERT, SELECT) to improve readability.

## 3️⃣ Connecting MySQL to Python

#### Install the official connector:
```Python
pip install mysql-connector-python
```
Then use it in your Python code:
```Python
import mysql.connector
```
# connect to the database
```Python
mydb = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='learn'
)

# create a cursor
my_cursor = mydb.cursor()

# insert data
my_cursor.execute("INSERT INTO people VALUES ('Fatemeh', 8, 'F')")

# commit changes
mydb.commit()

# close the connection
mydb.close()
```
## 4️⃣ Reading and Modifying Data

### Reading all rows
```Python
my_cursor.execute("SELECT * FROM people")
rows = my_cursor.fetchall()
for row in rows:
    print(row)
```

### Deleting Data:
```Python
DELETE FROM people WHERE name = 'Fatemeh' LIMIT 2;
```
### **💡 Always remember:**

**For security reasons, set a strong username and password for your database!**

## 5️⃣ SQL vs NoSQL Databases

| Type                  | Examples                   | Description                                 | Use Case              |
| --------------------- | -------------------------- | ------------------------------------------- | --------------------- |
| **Relational (SQL)**  | MySQL, MariaDB, PostgreSQL | Structured tables, fixed schema             | Banking, ERP systems  |
| **Document Store**    | MongoDB                    | Stores JSON-like documents, dynamic schema  | E-commerce apps       |
| **Graph Database**    | Neo4j                      | Stores relationships as edges between nodes | Social networks       |
| **Key-Value Store**   | Redis                      | Fast access to key-value pairs              | Caching, sessions     |
| **Wide Column Store** | Cassandra, HBase           | Flexible columns and high scalability       | Big Data applications |

🧠 SQL → Structured Query Language
⚡ NoSQL → Non-relational databases (Agile, highly scalable)

## 6️⃣ Summary

Use mysql-connector-python for database interaction in Python.

Use commit() to save changes and close() to release the connection.

Always validate and sanitize your SQL inputs to prevent SQL Injection.

Choose your database type based on data structure and scalability needs.

## 7️⃣ Reading Data from MySQL in Python

Here’s a complete example that shows how to **read** and **display** data from your MySQL database.

```python
import mysql.connector

# Connect to your database
mydb = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='learn'
)

# Create a cursor
my_cursor = mydb.cursor()

# Example of inserting a record (optional)
# my_cursor.execute("INSERT INTO people VALUES ('Mina', 31, 'F')")
# mydb.commit()

# Select all data from the table
query = "SELECT * FROM people"
my_cursor.execute(query)

# Iterate through each row and print formatted results
for (name, age, sex) in my_cursor:
    print(f"{name} is {age} years old and a {sex}")

# Close the connection
mydb.close()
```

### 🧩 Notes:

Always use mydb.commit() after INSERT, UPDATE, or DELETE queries.

For SELECT queries, you can loop directly over the cursor as shown above.

Using formatted strings (f"{name}...") makes your output cleaner and readable.

### ✅ Output Example:
```python
Alireza is 33 years old and a M
Fatemeh is 8 years old and a F
Mina is 31 years old and a F
```
#### ✨ That’s how you safely connect, read, and display data from your MySQL database using Python.
