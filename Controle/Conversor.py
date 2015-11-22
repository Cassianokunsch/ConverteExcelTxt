# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""


import pandas as pd

import pandas as pd

# Abrindo o arquivo xlsx
xlsx = pd.ExcelFile("DadosdoLabview\\testecorreto.xlsx")

# Abrindo arquivo para salvar em txt
arq  = open("Convertido.txt", "w")

# Pegando a primeira coluna
sheet1 = xlsx.parse(0)

# Pegando o tamanho do numero de linha da primeira coluna
size_coluna = sheet1.icol(0).size

# Varrendo a coluna
for i in range(size_coluna):
    row = sheet1.irow(i).tolist()  # Transformando o dado da linha em uma lista
    arq.write(str(row[0]))  # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
    arq.write("\n")  # Pulando uma linha no arquivo

arq.close()  # Fechando o arquivo