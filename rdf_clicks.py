'''
  Python script to extract the clickstream from Wikipedia data
  and to create an ontology
'''
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import RDF, FOAF

import hashlib

FILE = "2017_01_en_clickstream.tsv"
SEARCHTERM = "Martin_Luther"

g = Graph()

CLICK = Namespace("http://www.example.org/ns/click#")
g.bind("click", CLICK)

with open(FILE, 'rb') as f:
    data = f.readlines()
    for datum in data:
       line = datum.split("\t")
       if line[0] == SEARCHTERM:
           m = hashlib.sha224(line[1]+"prev").hexdigest()[15:]
           g.add( (URIRef(line[1]), RDF.type, CLICK.link) )
           g.add( (URIRef(m), RDF.type, URIRef(line[1])) )
           g.add( (URIRef(m), CLICK.prev, URIRef(line[0])) )
           g.add( (URIRef(m), CLICK.type, Literal(line[2])))
           g.add( (URIRef(m), CLICK.weight, Literal(line[3][:-2])))
       elif line[1] == SEARCHTERM:
           g.add( (URIRef(line[0]), RDF.type, CLICK.link) )
           m = hashlib.sha224(line[0]+"curr").hexdigest()[15:]
           g.add( (URIRef(m), RDF.type, URIRef(line[0])) )
           g.add( (URIRef(m), CLICK.curr, URIRef(line[1])) )
           g.add( (URIRef(m), CLICK.type, Literal(line[2])))
           g.add( (URIRef(m), CLICK.weight, Literal(line[3][:-2])))

g.serialize(destination='luther.ttl', format='xml')
