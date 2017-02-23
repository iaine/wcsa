'''
  Python script to extract the clickstream from Wikipedia data
  and to create an ontology
'''

FILE = "2017_01_en_clickstream.tsv"
SEARCHTERM = "Martin_Luther"

prev = {}
curr = {}
with open(FILE, 'rb') as f:
    data = f.readlines()
    for datum in data:
       line = datum.split("\t")
       if line[0] == SEARCHTERM:
           prev[line[1]] = line [3][:-2]
       elif line[1] == SEARCHTERM:
           curr[line[0]] = line [3][:-2]

print(prev)

print(curr) 
