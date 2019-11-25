#!/usr/bin/env python
from Bio import Entrez
from Bio import Medline
import re
import time
import sys
import numpy as np
TERM = sys.argv[1]
Entrez.email = sys.argv[3]
maxRes = int(sys.argv[2])
# VERIFICAR TOTAL
h = Entrez.esearch(db='pubmed', term=TERM)
record = Entrez.read(h)
MAX_COUNT = int(record['Count'])
batch_size = maxRes
t = []
h = Entrez.esearch(db='pubmed', retstart=0, retmax=batch_size, term=TERM)
result = Entrez.read(h)
ids = result['IdList']
h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
records = Medline.parse(h)
for record in records:
    ab = record.get('AB', '')
    ab = re.sub('\s+',' ',ab)
    ti = record.get('TI', '')
    ti = re.sub('\s+',' ',ti)
    pmid = record.get('PMID', '')
    aut = record.get('FAU', '')
    seperator = ';'
    aut = re.sub('\s+',' ',seperator.join(aut))
    t.append (pmid+'\t'+ti+'\t'+ab+'\t'+aut)
np.savetxt(sys.argv[4], t, delimiter='\t', fmt='%s')