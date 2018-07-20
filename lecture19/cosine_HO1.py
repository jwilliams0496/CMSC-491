import nltk
from bs4 import BeautifulSoup
import requests

def getPage(URL):
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html5lib')
    all_paras = soup.find_all('p')
    return str(all_paras)

def loadTDM(name, document):
    tdm[name] = {}
    
    for word in document.lower().split():
        tdm[name][word] = tc.tf_idf(word, document)
        
    return tdm

def cosDist(name1, name2):
    words1 = tdm[name1].copy()
    words2 = tdm[name2].copy()
    
    for word in words1:
        if word not in words2:
            words2[word] = 0
            
    for word in words2:
        if word not in words1:
            words1[word] = 0
            
    vName1 = [value for (words, value) in sorted(words1.items())]
    vName2 = [value for (words, value) in sorted(words2.items())]
    
    return nltk.cluster.util.cosine_distance(vName1, vName2)

def printSimilar(dist):
    if dist < .3:
        print ", the two are very similar"
    
    elif dist < .5:
        print ", the two are somewhat similar"
    
    elif dist > .8:
        print ", the two are very different"
    
    else:
        print ", the two are somewhat different"
        
    return
        
url1 = "http://swe.umbc.edu/~rayg/Econ1.html"
url2 = "http://swe.umbc.edu/~rayg/Econ2.html"
url3 = "http://swe.umbc.edu/~rayg/Econ3.html"

docA = getPage(url1)
docB = getPage(url2)
docC = getPage(url3)

all_docs = [docA.lower().split(), docB.lower().split(), docC.lower().split()]
titles = {"1":"docA", "2":"docB", "3":"docC"}
tc = nltk.TextCollection(all_docs)

tdm = {}
loadTDM("docA", docA)
loadTDM("docB", docB)
loadTDM("docC", docC)

dist = cosDist("docA", "docB")
print "distance from a to b, ", dist, printSimilar(dist)

dist = cosDist("docA", "docC")
print "distance from a to c, ", dist, printSimilar(dist)

dist = cosDist("docB", "docC")
print "distance from b to c, ", dist, printSimilar(dist)