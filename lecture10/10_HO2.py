import twitter
import json
from collections import Counter
from prettytable import PrettyTable

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
    
q = '@twitterapi'

count = 10

tweets = tw.search.tweets(q = q, count = count, lang = 'en')

texts = []

for status in tweets["statuses"]:
    texts.append(status["text"])

print texts

print "==================================================================="
words = []

for text in texts:
    for w in text.split():
        words.append(w)

print words

cnt = Counter(words)

pt = PrettyTable(field_names = ['Word', 'Count'])
srtCnt = sorted(cnt.items(), key = lambda pair: pair[1], reverse = True)

for kv in srtCnt:
    pt.add_row(kv)
    
print pt

print "==================================================================="

print "Lexical Diversity"
print 1.0 * len(set(words)) / len(words)