from datetime import datetime

birthdate = input().strip()

try:
    birth_date = datetime.strptime(birthdate, "%Y/%m/%d")
except ValueError:
    print("WRONG")
    exit()

today = datetime.now()

if birth_date > today:
    print("WRONG")
    exit()

user_age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    user_age -= 1

print(user_age)
