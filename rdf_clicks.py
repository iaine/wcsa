'''
  Python script to extract the clickstream from Wikipedia data
  and to create an ontology
'''
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import RDF, FOAF, XSD

import hashlib

FILE = "/home/iain/wikipedia/2017_01_en_clickstream.tsv"
SEARCHTERM = "Martin_Luther"

g = Graph()

CLICK = Namespace("http://www.example.org/ns/click#")
g.bind("click", CLICK)

def _set_hash(hash_string):
    '''
       Create hash for URI
    '''
    return hashlib.sha224(hash_string).hexdigest()[15:]

with open(FILE, 'rb') as f:
    data = f.readlines()
    for datum in data:
       line = datum.split("\t")
       if line[0] == SEARCHTERM:
           m = URIRef(_set_hash(line[1]+"prev"))
           g.add( (URIRef(line[1]), RDF.type, CLICK.link) )
           g.add( (m, RDF.type, URIRef(line[1])) )
           g.add( (m, CLICK.prev, URIRef(line[0])) )
           g.add( (m, CLICK.type, Literal(line[2])))
           g.add( (m, CLICK.weight, Literal(line[3][:-2], datatype=XSD.integer)))
       elif line[1] == SEARCHTERM:
           g.add( (URIRef(line[0]), RDF.type, CLICK.link) )
           m = URIRef(_set_hash(line[0]+"curr"))
           g.add( (m, RDF.type, URIRef(line[0])) )
           g.add( (m, CLICK.curr, URIRef(line[1])) )
           g.add( (m, CLICK.type, Literal(line[2])))
           g.add( (m, CLICK.weight, Literal(line[3][:-2], datatype=XSD.integer)))

g.serialize(destination='luther.ttl', format='xml')
