#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Bio import Entrez
from Bio import Medline
import re
import sys
import time
import numpy as np
try:
    from urllib.request import URLError

except:
    from urllib2 import URLError

TERM = sys.argv[1]
Entrez.email = sys.argv[2]
# VERIFICAR TOTAL
h = Entrez.esearch(db='pubmed', term=TERM)
record = Entrez.read(h)
MAX_COUNT = int(record['Count'])
batch_size = 5000
r=[]
# FAZER DOWNLOAD
print('0/'+str(MAX_COUNT))
for start in range(0, MAX_COUNT, batch_size):
    tudoCerto = False
    while tudoCerto == False:
        try:
            t = []
            h = Entrez.esearch(db='pubmed', retstart=start, retmax=batch_size, term=TERM)
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
                r.append ([pmid,ti,ab,aut])
            print(str(min([(start+batch_size),MAX_COUNT]))+'/'+str(MAX_COUNT))
            tudoCerto = True
        except URLError:
            print ('Problema na internet!')
            tudoCerto = False
            time.sleep(3)
        except:
            sys.exit()
        # se nao for o ultimo loop, aguardar 3 segundos antes de continuar
        if (start+batch_size) < MAX_COUNT:
            time.sleep(3)
# RESULTADO          
np.savetxt(sys.argv[3], r, delimiter='\t', fmt='%s')