import twitter
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
    
q = '#Microsoft, filter:images'

count = 100

search_results = tw.search.tweets(q = q, count = count)

statuses = search_results['statuses']

retweets = []

for status in statuses:
    if 'retweeted_status' in status:
        retweets.append((status['user']['screen_name'], status['retweet_count'], status['retweeted_status']['user']['screen_name'], status['text']))
        g = open('gmrTweet.txt', 'w')
        g.write(str(status))
        g.close
        
pt = PrettyTable(field_names = ['Usr', 'Count', 'rtUsr', 'text'])
[pt.add_row(row) for row in sorted(retweets, reverse = True)[:5]]

pt.max_width['text'] = 40
pt.align = 'l'
print pt