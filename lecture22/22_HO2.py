import facebook
import json
import requests
import nltk
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from collections import Counter
from prettytable import PrettyTable

def removeUnicode(text):
        asciiText = ""
        for char in text:
            if (ord(char) < 128):
                asciiText = asciiText + char
                
        return asciiText
    
ACCESS_TOKEN = 'EAACEdEose0cBADNjIOlshfElxgfq92lgXtYZB4KXhLBiNBUONQ1ZCXs7k9pZAgW0CjLdFTH9MW1LZAJJ7HN4RBfSCqgbZAjxmMorZAAtRed4hgLxxQnoVDsb64zbzZBc2OlmVZAX3L7yB4aBjg1XAkAxZCJ4iF27UuUdVXAN8Wo9pmBpdVonos4vuPUvYaHQSIgQZD'

fb = facebook.GraphAPI(ACCESS_TOKEN)

get_fields = ['id', 'message', 'created_time', 'caption', 'shares', 'likes.summary(true)', 'comments']

get_fields = ','.join(get_fields)

djt = fb.request('search', {'q':'Intel', 'type':'page', 'limit':5})
print json.dumps(djt, indent = 1)

Intel = '22707976849'

d_posts = fb.get_connections(Intel, 'posts', fields=get_fields)

print "The post text is:\n", removeUnicode(d_posts['data'][0]['message'])
print "Likes count is ", d_posts['data'][0]['likes']['summary']['total_count']

asc_2018 = ""
posts = d_posts['data']

for i in range(0,4):
    print "Post ", i+1, " is: ", posts[i]['message'].encode('utf-8')
    asc_2018 = asc_2018 + removeUnicode(posts[i]['message'])
    print "Like count is ", posts[i]['likes']['summary']['total_count']
    y = fb.get_connections(posts[i]['id'], 'likes')
    
vs_tot = 0
vs_pos = 0
vs_neg = 0
num_cmt = 0
y = fb.get_connections(posts[i]['id'], 'comments')

while True:
    try:
        yCmnt = {}
        print "Length of yCmnt is ", len(y['data'])
        for yCmnt in y['data']:
            print "Comments on post ", i+1, ": ", yCmnt['message'].encode('utf-8'), " at time", yCmnt['created_time']
            
            # start collecting text
            asc_2018 = asc_2018 + removeUnicode(yCmnt['message'])
            vs = vaderSentiment(yCmnt['message'].encode('utf-8'))
            print "---- Snetiment: " + str(vs['compound'])
            vs_tot = vs_tot + vs['compound']
            num_cmt = num_cmt + 1
            
            if (vs['compound'] < 0):
                vs_neg = vs_neg + 1
            
            else:
                vs_pos = vs_pos + 1
                
        print "----"
        y = requests.get(y['paging']['next']).json()
        
    except:
        print "no more comments"
        break
    
print "END OF POST ", i + 1
print "===================="

print "Overall sentiment is %f, pos %d, neg %d" % ((vs_tot/num_cmt), vs_pos, vs_neg)

skips = ["and", ",", "to", "the", "for", "in", "of", "that", "a", "on", "is", "get", "you", "has", "as",
         "at", "are", "", "an", "with", "will", "not", "have", "would", "so", "", "but", ":", "be", "like",
         "if", "should", "also", "there", "or", "by", "per", "they", "only", "can", "I", "who", "this",
         "it", "from", "one", "their", "The", "then", "his", "J", "we", "If", "?", "!"]

lstSent = nltk.tokenize.sent_tokenize(asc_2018)

words = []

for sentence in lstSent:
    for word in nltk.tokenize.word_tokenize(sentence):
        words.append(word.lower())
        
mostFreq_str = ""

for gmrWord in words:
    if gmrWord not in skips:
        mostFreq_str = mostFreq_str + gmrWord
        
frqDist = nltk.FreqDist(words)
print "dfeq", type(frqDist)

word_cnt = 0

for item in frqDist.items():
    word_cnt = word_cnt + item[1]
    
unique_word_cnt = len(frqDist.hapaxes())
hapaxNo = len(frqDist.hapaxes())

mostFreq = []

for w in frqDist.items():
    if w[0] not in skips:
        mostFreq.append(w)

print "Facebook Page Comments"
print 'Num lstSent:'.ljust(25), len(lstSent)
print 'Num Words:'.ljust(25), word_cnt
print 'Num Unique Words:'.ljust(25), unique_word_cnt
print 'Lexical Diversity is %f' % (1.0 * unique_word_cnt / word_cnt)
print 'Num Hapaxes:'.ljust(25), hapaxNo
print "The most frequent words follow"

mostFreq.sort(key=lambda c: c[1])

for w in mostFreq[-10:]:
    print w[0].encode('utf-8'), "\thas a count of ", w[1]