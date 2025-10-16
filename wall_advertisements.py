from bs4 import BeautifulSoup
import requests

url = 'https://divar.ir/s/tehran'
browsing_response = requests.get(url)

divar_soap = BeautifulSoup(browsing_response.text, 'html.parser')
ladder_tags = divar_soap.find_all('div', attrs={'class': 'kt-post-card'})

for ads in ladder_tags:
    ladder_tag = ads.find('span', attrs={'class': 'kt-post-card__red-text'})
    if ladder_tag and 'نردبان شده' in ladder_tag.text:
        ads_title = ads.find('h2', attrs={'class': 'kt-post-card__title'})
        if ads_title:
            print(ads_title.text.strip())
