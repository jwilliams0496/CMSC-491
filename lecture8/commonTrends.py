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
gmrPycon = tw.search.tweets(q = "feces")

for status in gmrPycon["statuses"]:
    print removeUnicode(status["text"])
    print "==="
    
def trendSetter(trends):
    setX = set()
    for trend in trends:
        setX.add(trend["name"])
        
    return setX

US_WOEID = 23424977
UK_WOEID = 23424975

setUS = set()
setUK = set()

usTrends = tw.trends.place(_id=US_WOEID)
setUS = trendSetter(usTrends[0]["trends"])

ukTrends = tw.trends.place(_id=UK_WOEID)
setUK = trendSetter(ukTrends[0]["trends"])

commonTrends = setUS.intersection(setUK)
print "commons: ", commonTrends

uniqueTrendsUS = setUS.difference(setUK)
print
print "US unique trends: ", uniqueTrendsUS