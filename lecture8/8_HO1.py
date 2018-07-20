import twitter
import json
import requests
import html5lib
from bs4 import BeautifulSoup

def removeUnicode(text):
        asciiText = ""
        for char in text:
            if (ord(char) < 128):
                asciiText = asciiText + char
                
        return asciiText

#Variables that contains the user credentials to access Twitter API 
oauth_token = "64652581-QGWS0czNA5UsF6REpXShFNTcApoxjUu6wUaLtWMJP"
oauth_token_secret = "wvB05sfRXDW8OmLlYsiCh8rlZldBQszPFO4tQiteXaC45"
consumer_key = "nq5XIMHxz7uE18AohfR9l0iZb"
consumer_secret = "ZcJzVAjII3oEpdIwkhdhmeB0jhE4NlgJ8y4ZGOpeAZIp6Eo89Q"

auth = twitter.oauth.OAuth(oauth_token, oauth_token_secret, consumer_key, consumer_secret)

tw = twitter.Twitter(auth=auth)

# Search
gmrPycon = tw.search.tweets(q = "antartica")

for status in gmrPycon["statuses"]:
    print removeUnicode(status["text"])
    print "==="
    
URL = "https://twitter.com/search?q=%40twitterapi&src=typd"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html5lib')
fp_text = soup.find_all('p')

print fp_text
all_paras = soup.find_all('p')

for para in all_paras:
    print para.text.encode('utf-8')
    
q = '@twitterapi'
count = 100

for status in tw.search.tweets(q = q, count = count)["statuses"]:
    if status["lang"] == 'en':
        print json.dumps(status["text"]).encode('utf-8')