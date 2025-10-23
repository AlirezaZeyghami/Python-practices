from bs4 import BeautifulSoup
import requests
import mysql.connector
from sklearn.tree import DecisionTreeRegressor


web_url = 'https://www.scrapethissite.com/pages/simple/'
scraped_page = requests.get(web_url)
soup = BeautifulSoup(scraped_page.text, "html.parser")

world_map = soup.find_all('div', attrs={'class': 'col-md-4 country'})


map_info = []
for country in world_map[:20]:
    country_name = country.find('h3', attrs={'class': 'country-name'})
    capital_name = country.find('span', attrs={'class': 'country-capital'})
    population = country.find('span', attrs={'class': 'country-population'})
    area = country.find('span', attrs={'class': 'country-area'})

    country_name = country_name.text.strip() if country_name else 'Unknown'
    capital_name = capital_name.text.strip() if capital_name else 'Unknown'
    population_txt = population.text if population else '0'
    area_txt = area.text if area else '0'

    try:
        population_val = float(population_txt.replace(',', '').strip())
        area_val = float(area_txt.replace(',', '').strip())
    except ValueError:
        population_val = 0
        area_val = 0

    map_info.append([country_name, capital_name, population_val, area_val])

try:
    fp_db = mysql.connector.connect(
        user='********',
        password='********',
        host='localhost',
        database='world_map'
    )
    cursor = fp_db.cursor()

    queri = "INSERT INTO countries (country, capital, population, area) VALUES (%s, %s, %s, %s)"

    for country, capital, population, area in map_info:
        try:
            cursor.execute(queri, (country, capital, population, area))
        except mysql.connector.Error as err:
            print(f"Failed inserting: {err}")
    fp_db.commit()
    print("Successfully inserted")

except Exception as err:
    print(f"Something went wrong: {err}")

finally:
    if 'fp_db' in locals() and fp_db.is_connected():
        cursor.close()
        fp_db.close()

x = [[row[2]] for row in map_info]
y = [row[3] for row in map_info]

clf = DecisionTreeRegressor()
here_clf = clf.fit(x, y)

answer = here_clf.predict([[85000000]])
print(answer)
