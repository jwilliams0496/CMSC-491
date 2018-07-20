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
    
nltk.download('stopwords')

QRY = ['incomes', 'families', 'economy']

html = requests.get("https://swe.umbc.edu/~rayg/econ_plan.html")

soup = BeautifulSoup(html.text, 'html5lib')

all_paras = soup.find_all('p')

data_2018 = ""

for para in all_paras:
    data_2018 = data_2018 + para.text
    
asc_2018 = removeUnicode(data_2018)

lstSent = nltk.tokenize.sent_tokenize(asc_2018)

sentences = [sent.lower().split() for sent in lstSent]

tc = nltk.TextCollection(sentences)

for sentNo in range(len(sentences)):
    tfidf = 0

    for term in [t.lower() for t in QRY]:
        tfidf = tfidf + tc.tf_idf(term, sentences[sentNo])
    
    if tfidf > 0:
        print "TF/IDF score %s for this sentence" % tfidf
        print "".join(sentences[sentNo])
        print