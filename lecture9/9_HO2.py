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

q = '@twitterapi'
count = 1

tweets = tw.search.tweets(q = q, count = count, lang = 'en')
for item in tweets["statuses"][0]["entities"]:
    print item, tweets["statuses"][0]["entities"][item]
    
print "================================================="

if tweets["statuses"][0]["entities"]["user_mentions"]:
    for field in tweets["statuses"][0]["entities"]["user_mentions"]:
        print field
    print "================================================="
    print tweets["statuses"][0]["entities"]["user_mentions"][0]["id_str"]
    
else:
    print "no user mentions this go round"
    
print " "

if tweets["statuses"][0]["entities"]["urls"]:
    print tweets["statuses"][0]["entities"]["urls"]
    
else:
    print "no urls this go round"
    
print " "

if tweets["statuses"][0]["entities"]["hashtags"]:
    print tweets["statuses"][0]["entities"]["hashtags"][0]["text"]
    
else:
    print "no hashtags this go round"