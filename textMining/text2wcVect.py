#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sys import argv
import pandas as pd
from sklearn.feature_extraction import text
#my_stop_words = list(pd.read_csv('stopwords.txt',header=None)[0])
text = list(pd.read_csv(argv[1],sep='\t',header=None)[0].astype('U'))
vectorizer = CountVectorizer(encoding='utf-8',stop_words='english',lowercase=True)
vectorizer.fit_transform(text)
vector = vectorizer.transform(text)
wl = vectorizer.get_feature_names()
np.savetxt(argv[2], wl, delimiter=",", fmt='%s')
np.savetxt(argv[3], vector.toarray(), delimiter=",", fmt='%s')
