import numpy as np
from sys import argv
import re
import pandas as pd
X = np.array((pd.read_csv(argv[1],sep='\t',header=None)))
idx=np.array(re.split(',',argv[2])).astype(int)
np.savetxt(argv[3], X[:,idx], delimiter="\t", fmt='%s')