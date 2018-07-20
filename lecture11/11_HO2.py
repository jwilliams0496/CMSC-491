from twython import TwythonStreamer
from collections import Counter
import datetime
import time
import string
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
        
        if len(tweets) >= 10:
            self.disconnect()
            
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
        
oauth_token = "64652581-QGWS0czNA5UsF6REpXShFNTcApoxjUu6wUaLtWMJP"
oauth_token_secret = "wvB05sfRXDW8OmLlYsiCh8rlZldBQszPFO4tQiteXaC45"
consumer_key = "nq5XIMHxz7uE18AohfR9l0iZb"
consumer_secret = "ZcJzVAjII3oEpdIwkhdhmeB0jhE4NlgJ8y4ZGOpeAZIp6Eo89Q"

stream = MyStreamer(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

gmrCnt = 1
while(gmrCnt == 1):
	tweets = []
	gmrStart = str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
	stream.statuses.filter(track = 'healthcare')
	gmrEnd = str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)
	with open("umbc.txt", "a") as myfile:
		for gmrText in tweets:
			if(gmrText["user"]["description"] is not None) and (gmrText["user"]["location"] is not None):
				myfile.write(str(gmrText["id"]))
				myfile.write(", ")
				rplText = string.replace(gmrText["text"].encode('utf-8'), "\r", "<cr>")
				myfile.write(string.replace(rplText, "\n", "<nl>"))
				myfile.write(", ")
				rplDesc = string.replace(gmrText["user"]["description"].encode('utf-8'), "\r", "<cr>")
				myfile.write(string.replace(rplDesc, "\n", "<nl>"))
				myfile.write(", ")
				myfile.write(gmrText["user"]["location"].encode('utf-8'))
				myfile.write(", ")
				myfile.write(gmrStart)
				myfile.write(", ")
				myfile.write(gmrEnd)
				myfile.write("\n")
				print gmrText["text"].encode('utf-8'),
				vs = vaderSentiment(gmrText["text"].encode('utf-8'))
				print "\n\t" + str(vs['compound'])
		gmrCnt = 2
		time.sleep(30)
        