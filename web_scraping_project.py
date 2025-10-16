from bs4 import BeautifulSoup
import requests
import mysql.connector

web_url = 'https://www.scrapethissite.com/pages/simple/'
scraped_page = requests.get(web_url)
soup = BeautifulSoup(scraped_page.text, "html.parser")

world_map = soup.find_all('div', attrs={'class': 'col-md-4 country'})

counter = 0
map_info = []
for country in world_map:
    if counter < 20:
        counter += 1
        country_name = country.find('h3', attrs={'class': 'country-name'})
        capital_name = country.find('span', attrs={'class': 'country-capital'})
        population = country.find('span', attrs={'class': 'country-population'})
        area = country.find('span', attrs={'class': 'country-area'})
        map_info.append([country_name.text.strip(), capital_name.text.strip(), population.text.strip(), area.text.strip()])

try:
    fp_db = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='world_map'
    )
    cursor = fp_db.cursor()

    queri = "INSERT INTO countries (country, capital, population, area) VALUES (%s, %s, %s, %s)"

    for _ in map_info:
        country, capital, population, area = _

        try:
            cursor.execute(queri, (country, capital, population, area))
            fp_db.commit()
            print("Successfully inserted")
        except mysql.connector.Error as err:
            print(f"Failed inserting: {err}")

except Exception as err:
    print(f"Something went wrong: {err}")

finally:
    if fp_db in locals() and fp_db.is_connected():
        cursor.close()
        fp_db.close()
