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

print "==========================================================="

if tweets["statuses"][0]["user"]:
    print tweets["statuses"][0]["user"].keys()
    print tweets["statuses"][0]["user"]["screen_name"].encode('utf-8')
    print tweets["statuses"][0]["user"]["description"].encode('utf-8')
    print tweets["statuses"][0]["user"]["location"].encode('utf-8')
    print "================================================================="
    
else:
    print "no user data this go round"
    