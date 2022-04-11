from bs4 import BeautifulSoup as bs
import requests
import re

DOMAIN = "https://www2.census.gov/"
URL = "https://www2.census.gov/geo/tiger/TIGER2019/PLACE/"


def get_soup(URL):
    return bs(requests.get(URL).text, 'html.parser')

for link in get_soup(URL).findAll("a", attrs={'href': re.compile(".zip")}):
    file_link = link.get('href')
    print(file_link)

with open('C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip', 'wb') as file:
    response = requests.get(DOMAIN + file_link)
    file.write(response.content)