import requests
import html5lib
from bs4 import BeautifulSoup

URL = "https://www.bitandbauble.com/home/2017/6/1/3-ingredient-tropical-ice-cream"

webpage = requests.get(URL)

print type(webpage)

html = webpage.text

print type(html)

soup = BeautifulSoup(html, 'html5lib')
print type(soup)