genres = {"Horror": [], "Romance": [], "Comedy": [], "History": [], "Adventure": [], "Action": []}


def get_people_and_survey():
    people_number = int(input())
    for _ in range(people_number):
        name, servey1, servey2, servey3 = map(str, input().split())
        genres[servey1].append(name)
        genres[servey2].append(name)
        genres[servey3].append(name)


get_people_and_survey()
sorted_genres = sorted(genres.items(), key=lambda x: (-len(x[1]), x[0]))

for genres, people in sorted_genres:
    print(f"{genres} : {len(people)}")
