#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from Bio import Entrez
from Bio import SeqIO
from time import sleep
from sys import argv

try:
    # For Python 3.0 and later
    from urllib.request import URLError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import URLError
    
 
# É interessante informar um email real. É uma medida de segurança para o
# NCBI saber de quem é a requisição.
Entrez.email = argv[2] #"A.N.Other@example.com"
 
# O termo de busca é necessário em dois momentos
# neste script, por isso é interessante designá-lo para uma variável,
# evitando a necessidade de repetir todo o termo de busca duas vezes.
TERM=argv[1] #"herbaspirillum[organism] AND nitrogen"
 
# Uma busca é previamente feita para verificar quantas sequências o termo retorna
handle = Entrez.esearch(db='protein', term=TERM)
record = Entrez.read(handle)
MAX_COUNT = int(record['Count'])
 
# batch_size armazena o número de sequências que serão baixadas
# por ciclo de download. Deve ser no máximo 10000.
batch_size = 1000
 
# Aqui são executados os ciclos para baixar todos as sequências,
# contornando o problema do limite de resultados que podem ser baixados.
# Na variável seqs são armazenadas as sequências após cada iteração,
# para no final salvar todas em um arquivo único.
seqs = [ ]
# A próxima linha exibe um texto para iniciar a contagem com
# o número de sequências já baixadas.
print('0/'+str(MAX_COUNT))
for start in range(0, MAX_COUNT, batch_size):
    tudoCerto = False
    while tudoCerto == False:
        try:
            # Em cada iteração é definido um ponto start de download,
            # através do parâmetro retstart.
            handle = Entrez.esearch(db='protein', retstart=start, retmax=batch_size, term=TERM)
            record = Entrez.read(handle)
            seq_handle = Entrez.efetch(db="protein", rettype="fasta", id=record["IdList"])
            seq_record = SeqIO.parse(seq_handle, "fasta")
            seq_list = list(seq_record)
            
            # Uma nova linha com a contagem de sequências já baixadas é exibida em cada loop.
            print(str(min([(start+batch_size),MAX_COUNT]))+'/'+str(MAX_COUNT))
            tudoCerto = True
        except URLError:
            print ('Problema na internet!')
            tudoCerto = False
            sleep(3)

        # se nao for o ultimo loop, aguardar 3 segundos antes de continuar
        if (start+batch_size) < MAX_COUNT:
            sleep(1)
    seqs.extend(seq_list)

# Salvar o resultado em um arquivo FASTA de nome "resultado.fasta".
SeqIO.write(seqs, argv[3], "fasta")
