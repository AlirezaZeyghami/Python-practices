import re

user_email = input()


def correct_email(email):
    correct_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(correct_pattern, email) is not None


if correct_email(user_email):
    print("OK")
else:
    print("WRONG")
