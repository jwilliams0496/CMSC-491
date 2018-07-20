from bs4 import BeautifulSoup
import requests
import json
import codecs
import nltk

def removeUnicode(text):
    asciiText = ""
    for char in text:
        if (ord(char) < 128):
            asciiText = asciiText + char
                
    return asciiText
    
fileObj = codecs.open("16_HO1.rtf", "w", "UTF")

html = requests.get("https://www.bitandbauble.com/home/2017/6/1/3-ingredient-tropical-ice-cream")

soup = BeautifulSoup(html.text, 'html5lib')

all_paras = soup.find_all('p')

data_2017 = ""

for para in all_paras:
   fileObj.write(para.text)
   data_2017 = data_2017 + para.text
   asc_2017 = removeUnicode(data_2017)
   
lstSent = nltk.tokenize.sent_tokenize(asc_2017)
print type(lstSent), "sent type"

words = []
for sentence in lstSent:
    for word in nltk.tokenize.word_tokenize(sentence):
        words.append(word.lower())
        
frqDist = nltk.FreqDist(words)
print "dfreq", type(frqDist)

word_cnt = 0
for item in frqDist.items():
    word_cnt = word_cnt + item[1]
    
unique_word_cnt = len(frqDist.keys())

hapaxNo = len(frqDist.hapaxes())

skips = ["and", ".", "to", ",", "the", "for", "in", "of", "that", "a", "on", "is",\
         "get", "you", "has", "as", "at", "are", "", "an", "with", "will", "not",\
         "have", "would", "would", "so", "'", "but", ":", "be", "like", "if", "should",\
         "also", "there","or", "by", "per"]

mostFreq = []
for w in frqDist.items():
    if w[0] not in skips:
        mostFreq.append(w)
            
print "Antartica Findings"
print "Num lstSent:".ljust(25), len(lstSent)
print "Num Words:".ljust(25), word_cnt
print "Num Unique Words:".ljust(25), unique_word_cnt
print "Num Hapaxes:".ljust(25), hapaxNo
print "The most frequent words follow"

mostFreq.sort(key = lambda c: c[1])

for w in mostFreq[-10]:
    print w[0].encode('utf-8'), "\thas a count of ", w[1]