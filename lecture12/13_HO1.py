import _pickle as pickle

try:
    input = raw_input
    
except NameError:
    pass

with open(, 'rb') as gmrIn:
    model = pickle.load(gmrIn)
    classifier = model['classifier']
    vectorizer = model['vectorizer']
    mlb = model['mlb']
    
while True:
    print "Ask a question, or type exit."
    gmrInput = input('> ')
    
    if gmrInput == 'exit':
        exit()
    
    else:
        V = vectorizer.transform([gmrInput])
        
        for gmrV in V:
            print "gmrV \n", gmrV
            
        print "Your question is: ", gmrInput
        prediction = classifier.predict(V)
        
        for gmrP in prediction:
            for gmrPred in gmrP:
                if gmrPred > 0:
                    print "gmrPred ", gmrPred
                    
        tags = mlb.inverse_transform(prediction)[0]
        print "MLB ", mlb.inverse_transform(prediction)[0]
        tags = ', '.join(tags)
        
        if tags:
            print "Predicted tags: ", tags
            
        else:
            print "No tag for this question"