import twitter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

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

# 10 tweets from Coke
print "\n25 Tweets with \'@cocacola\'"
q = '@cocacola'

count = 25

tweets = tw.search.tweets(q = q, count = count, lang = 'en')

for status in tweets["statuses"]:
    
    words = []
    
    for w in removeUnicode(status['text']).split():
        words.append(w)
        

    vs = vaderSentiment(status["text"].encode('utf-8'))

    print "\n========================\n"    
    print removeUnicode(status['text'])
    print "\nLexical Diversity: ", 1.0 * len(set(words)) / len(words)
    print "Sentiment: " + str(vs['compound'])
    
print "\n\n======================================================================="
    
# 10 tweets from Pepsi
print "\n\n25 Tweets with \'@pepsi\'"

q = '@pepsi'
count = 25

tweets = tw.search.tweets(q = q, count = count, lang = 'en')

for status in tweets["statuses"]:
    
    words = []
    
    for w in removeUnicode(status['text']).split():
        words.append(w)
        

    vs = vaderSentiment(status["text"].encode('utf-8'))

    print "\n========================\n"    
    print removeUnicode(status['text'])
    print "\nLexical Diversity: ", 1.0 * len(set(words)) / len(words)
    print "Sentiment: " + str(vs['compound'])