from datetime import datetime

birthdate = input().strip()

try:
    year, month, day = map(int, birthdate.split("/"))
    birth_date = datetime(year, month, day)
except ValueError:
    print("WRONG")
    exit()

today = datetime.now()

user_age = today.year - birth_date.year

print(user_age)
