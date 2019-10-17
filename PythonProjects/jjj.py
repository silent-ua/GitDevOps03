from bs4 import BeautifulSoup
import requests


BASE_URL = 'https://www.pexels.com/search'
URL = f'{BASE_URL}/landscape'

doc = requests.get(URL)
soup = BeautifulSoup(doc.text, 'html.parser')


result = []

for i in soup.find_all('article', class_='photo-item'):
