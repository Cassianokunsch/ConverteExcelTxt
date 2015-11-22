# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""

from PyQt4 import QtCore, QtGui
import sys

class AplicativoConversor(QtGui.QMainWindow):
    def __init__(self):
        super(AplicativoConversor, self).__init__()
        self.setupUi()

    def setupUi(self):
        # SETANDO O TAMANHO MAXIMO
        self.resize(650, 350)

        # Widget principal
        self.centralWidget = QtGui.QWidget(self)

        # Layout pricipal
        self.LayoutPrincipal = QtGui.QHBoxLayout(self.centralWidget)
        self.LayoutPrincipal.setMargin(3)
        self.LayoutPrincipal.setSpacing(3)

        self.LayoutWidget = QtGui.QVBoxLayout()
        self.LayoutWidget.setMargin(3)
        self.LayoutWidget.setSpacing(3)

        # CRIANDO TODOS OS LAYOUTS
        self.layoutArqOri()
        self.layoutArqDes()
        self.layoutConversao()
        self.layoutBtnConversao()

        # ADICIONANDO TODOS OS LAYOUTS NO LAYOUT PRINCIPAL
        self.LayoutWidget.addLayout(self.LayoutArqOrigem)
        self.LayoutWidget.addLayout(self.LayoutArqDestino)
        self.LayoutWidget.addLayout(self.LayoutConversao)
        self.LayoutWidget.addLayout(self.LayoutBtnConversao)

        self.LayoutPrincipal.addLayout(self.LayoutWidget)

        self.setCentralWidget(self.centralWidget)

    def layoutArqOri(self):
        # LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqOrigem = QtGui.QHBoxLayout()
        self.LayoutArqOrigem.setMargin(3)
        self.LayoutArqOrigem.setSpacing(3)

        # BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        ## CRIANDO OS BOTOES
        self.LbSelectArq = QtGui.QLabel("Selecione o arquivo que quer converter:", self.centralWidget)
        self.LEditArqOrig = QtGui.QLineEdit(self.centralWidget)
        self.btn_browser1 = QtGui.QPushButton("Browser...", self.centralWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(("Imagens//pasta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_browser1.setIcon(icon)

        ## ADICIONANDO OS BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqOrigem.addWidget(self.LbSelectArq)
        self.LayoutArqOrigem.addWidget(self.LEditArqOrig)
        self.LayoutArqOrigem.addWidget(self.btn_browser1)

    def layoutArqDes(self):
        # LAYOUT DO SELECIONAR ARQUIVO DE DESTINO
        self.LayoutArqDestino = QtGui.QHBoxLayout()
        self.LayoutArqDestino.setMargin(3)
        self.LayoutArqDestino.setSpacing(3)

        # BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE DESTINO
        ## CRIANDO OS BOTOES
        self.LbArqDes = QtGui.QLabel("Selecione onde quer salvar o novo arquivo:", self.centralWidget)
        self.LEditArqDes = QtGui.QLineEdit(self.centralWidget)
        self.BtnBrowser2 = QtGui.QPushButton("Browser...", self.centralWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(("Imagens//pasta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnBrowser2.setIcon(icon)

        ## ADICIONANDO OS BOTOES DO LAYOUT DO SELECIONAR ARQUIVO DE ORIGEM
        self.LayoutArqDestino.addWidget(self.LbArqDes)
        self.LayoutArqDestino.addWidget(self.LEditArqDes)
        self.LayoutArqDestino.addWidget(self.BtnBrowser2)

    def layoutConversao(self):
        # LAYOUT DO QUE MOSTRA O STATUS DA CONVERSAO
        self.LayoutConversao = QtGui.QVBoxLayout()
        self.LayoutConversao.setMargin(3)
        self.LayoutConversao.setSpacing(3)

        # BOTOES DO LAYOUT QUE MOSTRA O STATUS DA CONVERSAO
        ## CRIANDO OS BOTOES
        self.CxTexto = QtGui.QTextEdit(self.centralWidget)
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 24)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA O STATUS DA CONVERSAO
        self.LayoutConversao.addWidget(self.CxTexto)
        self.LayoutConversao.addWidget(self.progressBar)

    def layoutBtnConversao(self):
        # LAYOUT DO QUE TEM OS BOTOES PARA SAIR E CONVERTER
        self.LayoutBtnConversao = QtGui.QHBoxLayout()
        self.LayoutBtnConversao.setMargin(3)
        self.LayoutBtnConversao.setSpacing(3)

        # BOTOES DO LAYOUT QUE TEM OS BOTOES PARA SAIR E CONVERTER
        ## CRIANDO OS BOTOES
        spacerItem = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.BtnConverter = QtGui.QPushButton(" Converter!", self.centralWidget)
        self.BtnConverter.clicked.connect(self.prints)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens//start_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnConverter.setIcon(icon1)

        self.BtnSair = QtGui.QPushButton(" Sair", self.centralWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens//log_out.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSair.setIcon(icon2)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA OS BOTOES DE CONVERTER E SAIR
        self.LayoutBtnConversao.addItem(spacerItem)
        self.LayoutBtnConversao.addWidget(self.BtnConverter)
        self.LayoutBtnConversao.addWidget(self.BtnSair)

    def prints(self):
        self.CxTexto.toPlainText()
        self.CxTexto.insertPlainText("Casa\n")
        self.CxTexto.moveCursor(QtGui.QTextCursor.End)

    def menu(self):
        self.menuBar = QtGui.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.setMenuBar(self.menuBar)

    def toolBar(self):
        self.mainToolBar = QtGui.QToolBar(self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

    def status(self):
        self.statusBar = QtGui.QStatusBar(self)
        self.setStatusBar(self.statusBar)

if __name__ == "__main__":
    root = QtGui.QApplication(sys.argv)
    app = AplicativoConversor()
    app.show()
    root.exec_()