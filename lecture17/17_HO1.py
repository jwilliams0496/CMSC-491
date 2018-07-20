from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

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
    
fileObj = codecs.open("17_HO1.rtf", "w", "UTF")
html = requests.get("http://swe.umbc.edu/~rayg/econ_plan.html")
url = "http://swe.umbc.edu/~rayg/econ_plan.html"
soup = BeautifulSoup(html.text, 'html5lib')
all_paras = soup.find_all('p')

# Write test to file and collate it into a str var
data_2017 = ""

for para in all_paras:
    fileObj.write(para.text)
    data_2017 = data_2017 + para.text

parser = HtmlParser.from_url(url, Tokenizer('English'))    
stemmer = Stemmer('English')
summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words('English')

for sentence in summarizer(parser.document, 3):
    print (sentence)

#print "Summary of new iceberg"
#print "Print Three Sentence Summary"

#for sentence in Iceberg_sum['top_n_summary']:
#    print removeUnicode(sentence)