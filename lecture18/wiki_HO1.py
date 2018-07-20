from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import ne_chunk
import wikipedia

e = ""

topic = "Python (programming language)"
# topic = 'python'

try:
    entity = str(wikipedia.summary(topic, sentences = 4).encode('utf-8'))

    tokens = word_tokenize(entity)
    gmrTags = pos_tag(tokens)
    gmrChunks = ne_chunk(gmrTags, binary = True)

    print("Topic summary {}".format(topic))
    print entity
    print("= = = =")
    print("Topic has these noun phrases in 4 sentence summary: ")

    gmrNouns = []
    gmrPrev = None
    gmrPhrase = []

    for (token, pos) in gmrTags:
        if pos.startswith('NN'):
            if pos == gmrPrev:
                gmrPhrase.append(token)

            else:
                if gmrPhrase:
                    gmrNouns.append(token)
                gmrPhrase = [token]

        else:
            if gmrPhrase:
                gmrNouns.append((''.join(gmrPhrase), gmrPrev))
                gmrPhrase = []
                gmrPrev = pos
                        
            if gmrPhrase:
                gmrNouns.append((''.join(gmrPhrase), pos))
                        
            for noun in gmrNouns:
                print noun[0]
                        
            print("= = = =")
            print("Topic summary has these named entities, with description:")
            
            typeEntity ='NE'
            gmrEntity = []
                    
            for gmrNE in gmrChunks.subtrees():
                if gmrNE.label() == typeEntity:
                    tokens = [t[0] for t in gmrNE.leaves()]
                    gmrEntity.append(token[0])
                            
            gmrList = []
                    
            for gmrNE in gmrEntity:
                gmrList.append(gmrNE)
                        
            gmrSet = set(gmrList)
                    
            for item in gmrSet:
                print item

                try:
                    summary = wikipedia.summary(item, sentences = 1)
                    print("{}: {}".format(item, summary.encode('utf-8')))

                except wikipedia.exceptions.WikipediaException as e1:
                    print "This NE has multiple meanings in Wikipedia"
                    continue
                        
except wikipedia.exceptions.WikipediaException as e:
    print e
    print "Wikipedia says to disambiguate"
