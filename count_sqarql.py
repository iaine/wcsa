from rdflib import Graph


g = Graph()

g.parse("luther.ttl")

previous = '''
    select ?j ?k where
    {
    ?id click:prev ?o .
    ?id click:weight ?j .
    ?id rdf:type ?k .
    }
    ORDER BY DESC(?j)
    LIMIT 20
'''

current = '''
    select ?j ?k where
    {
    ?id click:curr ?o .
    ?id click:weight ?j .
    ?id rdf:type ?k .
    }
    ORDER BY DESC(?j)
    LIMIT 20
'''

data = g.query(previous)

for d in data:
    print(d)

data = g.query(current)

for d in data:
    print(d)
