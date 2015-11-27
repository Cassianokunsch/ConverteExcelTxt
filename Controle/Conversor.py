# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""
from time import strftime
import pandas as pd
import threading

class ThConversor(threading.Thread):
    def __init__ (self, dadosArquivo, diretorioArqOrigem):
        super(ThConversor, self).__init__()
        self.dados = dadosArquivo
        self.origem = diretorioArqOrigem

    def run(self):
        (Converte(self.origem, self.dados))


class Converte(object):
    def __init__(self, diretorioArqOrigem, dados):
        super(Converte, self).__init__()
        self.start(diretorioArqOrigem, dados)

    def start(self, diretorioArqOrigem, dados):
        # Abrindo o arquivo xlsx
        xlsx = pd.ExcelFile(diretorioArqOrigem)

        # Pegando a primeira coluna
        sheet1 = xlsx.parse(0)

        # Pegando o tamanho do numero de linha da primeira coluna
        size_coluna = sheet1.icol(0).size

        # Varrendo a coluna
        dados.append(size_coluna)
        for i in range(size_coluna):
            row = sheet1.irow(i).tolist()  # Transformando o dado da linha em uma lista
            dados.append(str(row[0]))

class SalvaArquivo(object):
    def __init__(self, diretorioArqDestino, lst_dados, obj):
        super(SalvaArquivo, self).__init__()
        self.objeto = obj
        self.salva(diretorioArqDestino, lst_dados)

    def salva(self, diretorioArqDestino, lst_dados):
        # Abrindo arquivo para salvar em txt
        arq  = open(diretorioArqDestino, "w")
        tamanho = lst_dados[0]
        del(lst_dados[0])
        for i in range(tamanho):
            arq.write(str(lst_dados[i]))  # Transformando o conteudo da primeira posicao da lista em string e escrevendo no arquivo
            arq.write("\n")  # Pulando uma linha no arquivo

        self.objeto.CxTexto.insertPlainText(strftime('[%H:%M:%S]')+ " Arquivo salvo com sucesso!!!\n")
        arq.close()  # Fechando o arquivo