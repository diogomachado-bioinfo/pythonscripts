# pythonscripts
Python scripts for various utilities are available here, especially: text mining, machine learning and bioinformatics.

clustering
--------------------------------------------------------------------------------------------------------------------------------
- getCluster.py: Returns the rows corresponding to a given cluster, considering a file with clustered indices.
Example: python getCluster.py data.txt clusIdx.txt 2 result.txt

- kmeans.py: Cluster with a specific k and return the resulting indexes.
Example: python kmeans.py data.txt 3 result.txt

ncbi
--------------------------------------------------------------------------------------------------------------------------------
- proteinDownload.py: Download a set of protein sequences from NCBI and generate a FASTA.
Example: python proteinDownload.py "herbaspirillum AND nitrogen" "A.N.Other@example.com" result.fasta

- pubmedDownload.py: Downloads an NCBI article dataset and generates a tabbed file.
Example: python pubmedDownload.py "herbaspirillum AND nitrogen" "A.N.Other@example.com" result.txt

- pubmedDownload_withMax.py: Download a set of NCBI protein sequences and generate a FASTA, considering an established result limit.
Example: python pubmedDownload_withMax.py "herbaspirillum AND nitrogen" 10 "A.N.Other@example.com" result.txt

textMining
--------------------------------------------------------------------------------------------------------------------------------
- porterStemmer.py: Receives a txt file and returns the texts handled by porterStemmer.
Example: python porterStemmer.py text.txt result.txt

- text2tfidfVect.py: Vectorizes the text in a txt file using tfidf.
Example: python text2tfidfVect.py text.txt result.txt

- text2wcVect.py: Vectorizes the text in a txt file using word count.
Example: python text2tfidfVect.py text.txt result.txt

utilities
--------------------------------------------------------------------------------------------------------------------------------
- getColumn.py: Receives a column-structured txt file and returns only the specified columns.
Example: python getColumn.py data.txt 0,3 result.txt

- regexLines.py: Performs regular expression search on all lines of a file.
Example: python regexLines.py text.txt "^[a-z]" result.txt
