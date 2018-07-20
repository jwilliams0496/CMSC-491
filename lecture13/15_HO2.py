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

html = open("test.htm", "r").read()
print type(html)

soup = BeautifulSoup(html, 'html5lib')
print type(soup)

fp_text = soup.p
fa_text = soup.a.text
ftd_text = soup.td.text
div_text = soup.div.text

print fp_text.encode('utf-8'),fa_text.encode('utf-8')
print soup.p.name, soup.a.name
print soup.a.attrs, soup.a['href']
print "P text is ", soup.p.text
print "TD is ", soup.ftd_text
print "div is ", soup.div.text

fp_txt = soup.find("p")
fa_txt= soup.find("a")
ftd_txt = soup.find("td")
div_txt = soup.find("div")

print "P is ", fp_txt
print "TD is ", ftd_txt
print "div is ", div_txt
print "a is ", fa_txt

bs4_txt = soup.find(text = "Beautiful Soup")
print "Beautiful Soup is ", bs4_txt

submit_id = soup.find(id = "sb_form_go")
print submit_id

stySearch = soup.find(id = "sb_form_go")
print stySearch

fp_all = soup.find_all("a")

for fp in fp_all:
    print fp.sting, "===AND===", fp.text.encode('utf-8')