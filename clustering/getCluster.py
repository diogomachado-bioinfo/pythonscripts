import numpy as np
from sys import argv
X = np.genfromtxt(argv[1], delimiter=',')
C = np.genfromtxt(argv[2], delimiter=',')
N = int(argv[3])
R = X[C==N]
np.savetxt(argv[4], R, delimiter=",", fmt='%s')