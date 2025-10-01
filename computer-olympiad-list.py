final_list = []

applicant_number = int(input())
for _ in range(applicant_number):
    gender, name, language = map(str, input().split("."))
    final_list.append([gender, name, language])

for i in final_list:
    i[1] = i[1].capitalize()

females = [applicant for applicant in final_list if applicant[0] == "f"]
males = [applicant for applicant in final_list if applicant[0] == "m"]

females.sort(key=lambda x: x[1])
males.sort(key=lambda x: x[1])

for person in females + males:
    print(f"{person[0]} {person[1]} {person[2]}")
