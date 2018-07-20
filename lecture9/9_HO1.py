import twitter

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
    
q = "Antartica"
 
count = 2
 
tweets = tw.search.tweets(q = q, count = count, lang = 'en')
 
for status in tweets["statuses"]:
    print status["text"].encode('utf-8')

print "================================================="

count = 1
tweets = tw.search.tweets(q = q, count = count, lang = 'en')

for item in tweets["statuses"]:
    print status["text"].encode('utf-8')

for item in tweets["search_metadata"]:
    print item, tweets["search_metadata"]
    
nextSet = tweets["search_metadata"]["next_results"]

next_MaxID = nextSet.split("max_id=")[1].split("&")[0]

print next_MaxID
print "================================================="

tweets = tw.search.tweets(q = q, count = count, include_entities = "true", max_id = next_MaxID)
print "================================================="

for status in tweets["statuses"]:
    print status["text"].encode('utf-8')