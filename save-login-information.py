import mysql.connector
import re


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None


def is_valid_password(password):
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return re.match(password_pattern, password) is not None


try:
    p2_db = mysql.connector.connect(
        user='********',
        password='********',
        host='localhost',
        database='my_users'
    )
    cursor = p2_db.cursor()

    username = input()
    while not is_valid_email(username):
        print("Right pattern of email: example@domain.com")
        username = input()

    password = input()
    while not is_valid_password(password):
        print("Right pattern of password include numbers, uppercase and lowercase letters")
        password = input()

    queri = "INSERT INTO new_users (username, password) VALUES (%s, %s)"
    values = (username, password)

    try:
        cursor.execute(queri, values)
        p2_db.commit()
        print("Successfully inserted new user")
    except mysql.connector.Error as err:
        print(f"Failed inserting new user: {err}")

except Exception as err:
    print(f"Something went wrong: {err}")

finally:
    if p2_db in locals() and p2_db.is_connected():
        cursor.close()
        p2_db.close()
