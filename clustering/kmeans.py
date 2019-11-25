from sklearn.cluster import KMeans
import numpy as np
from sys import argv
X = np.genfromtxt(argv[1], delimiter=',')
kmeans = KMeans(n_clusters=int(argv[2]), random_state=0).fit(X)
np.savetxt(argv[3], kmeans.labels_, delimiter=",", fmt='%i')