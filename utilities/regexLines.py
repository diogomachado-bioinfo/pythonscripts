import numpy as np
from sys import argv
import re
import csv
import pandas as pd
X = np.array((pd.read_csv(argv[1],sep='\t',header=None)))
X=X[:,0]
RL = np.vectorize (lambda x:re.search(argv[2],str(x)))
re_result = RL(X).astype(bool)
#print(np.where(re_result))
np.savetxt(argv[3], X[re_result], delimiter=",", fmt='%s')