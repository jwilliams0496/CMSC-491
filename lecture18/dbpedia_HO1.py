import rdflib

entity = "Blade_Runner"
entity = "Python_(programming_language"
#entity = "Python"

dbpedia_url = 'http://dbpedia.org/resource/{}'.format(entity)

grf = rdflib.Graph()
grf.parse(dbpedia_url)

query = (rdflib.URIRef(dbpedia_url),\
         rdflib.URIRef('http://dbpedia.org/ontology/wikiPageDisambiguates'),\
         None)

multiples = list(grf.triples(query))

if len(multiples) > 1:
    print ("Your topic {}".format(dbpedia_url))
    
    for subject, verb, object in multiples:
        print('----can mean : {}'.format(object))
        
else:
    query = (rdflib.URIRef(dbpedia_url),\
             rdflib.URIRef('http://dbpedia.org/ontology/abstract'),\
             None)
    
    summary = list(grf.triples(query))
    
    for subject, verb, object in summary:
        if object.language == 'en':
            print(object.encode('utf-8'))