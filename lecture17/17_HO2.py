import russell as ru
from bs4 import BeautifulSoup
from nltk import BigramAssocMeasures
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
    
fileObj = codecs.open("17_HO1.rtf", "w", "UTF")

html = requests.get("http://swe.umbc.edu/~rayg/econ_plan.html")

soup = BeautifulSoup(html.text, 'html5lib')

all_paras = soup.find_all('p')

# Write test to file and collate it into a str var
data_2017 = ""

for para in all_paras:
    fileObj.write(para.text)
    data_2017 = data_2017 + para.text
    
Iceberg_sum = ru.summarize(data_2017)

print "Summary of new iceberg"
print "Print Three Sentence Summary"

for sentence in Iceberg_sum['top_n_summary']:
    print removeUnicode(sentence)
    
asc_2017 = removeUnicode(data_2017)

bigWords = nltk.tokenize.word_tokenize(asc_2017)
N = 25
search = nltk.BigramCollocationFinder.from_words(bigWords)

search.apply_freq_filter(2)
search.apply_word_filter(lambda skips: skips in nltk.corpus.stopwords.words('English'))

idxJaccard = BigramAssocMeasures.jaccard
bigrams = search.nbest(idxJaccard, N)

for bigram in bigrams:
    print str(bigram[0]).encode('utf-8'), " ", str(bigram[1]).encode('utf-8')