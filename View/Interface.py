# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <21/11/2015>
"""

from PyQt4 import QtCore, QtGui
from Controle.Conversor import ThConversor, SalvaArquivo
import sys
from time import strftime

class AplicativoConversor(QtGui.QMainWindow):
    def __init__(self):
        super(AplicativoConversor, self).__init__()
        self.setupUi()

    def setupUi(self):
        # SETANDO O TAMANHO MAXIMO
        self.resize(675, 350)
        self.setMinimumSize(675, 350)
        self.setMaximumSize(675, 350)
        self.setWindowTitle("LEDS Conversor")

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
        self.layoutImagem()
        self.layoutArqOri()
        self.layoutArqDes()
        self.layoutConversao()
        self.layoutBtnConversao()

        # ADICIONANDO TODOS OS LAYOUTS NO LAYOUT PRINCIPAL
        self.LayoutWidget.addLayout(self.LayoutImagem)
        self.LayoutWidget.addLayout(self.LayoutArqOrigem)
        self.LayoutWidget.addLayout(self.LayoutArqDestino)
        self.LayoutWidget.addLayout(self.LayoutConversao)
        self.LayoutWidget.addLayout(self.LayoutBtnConversao)

        self.menu()
        self.toolBar()
        self.status()


        self.LayoutPrincipal.addLayout(self.LayoutWidget)

        self.setCentralWidget(self.centralWidget)

    def layoutImagem(self):
        self.LBImagem = QtGui.QLabel()
        self.LBImagem.setPixmap(QtGui.QPixmap(("Imagens//Title.png")))
        self.LBImagem.setAlignment(QtCore.Qt.AlignCenter)
        self.LayoutImagem =QtGui.QVBoxLayout(self.centralWidget)
        self.LayoutImagem.addWidget(self.LBImagem)

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
        self.btn_browser1.clicked.connect(self.arqOrigem)
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
        self.BtnBrowser2.clicked.connect(self.arqDestino)
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
        self.CxTexto = QtGui.QTextBrowser(self.centralWidget)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA O STATUS DA CONVERSAO
        self.LayoutConversao.addWidget(self.CxTexto)

    def layoutBtnConversao(self):
        # LAYOUT DO QUE TEM OS BOTOES PARA SAIR E CONVERTER
        self.LayoutBtnConversao = QtGui.QHBoxLayout()
        self.LayoutBtnConversao.setMargin(3)
        self.LayoutBtnConversao.setSpacing(3)

        # BOTOES DO LAYOUT QUE TEM OS BOTOES PARA SAIR E CONVERTER
        ## CRIANDO OS BOTOES
        spacerItem = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.BtnConverter = QtGui.QPushButton(" Converter!", self.centralWidget)
        self.BtnConverter.clicked.connect(self.start_conversor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens//start_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnConverter.setIcon(icon1)

        self.BtnSair = QtGui.QPushButton(" Sair", self.centralWidget)
        self.BtnSair.clicked.connect(self.close)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens//log_out.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSair.setIcon(icon2)

        ## ADICIONANDO OS BOTOES DO LAYOUT QUE MOSTRA OS BOTOES DE CONVERTER E SAIR
        self.LayoutBtnConversao.addItem(spacerItem)
        self.LayoutBtnConversao.addWidget(self.BtnConverter)
        self.LayoutBtnConversao.addWidget(self.BtnSair)

    def creat_progress_bar(self):
        self.pbar = QtGui.QProgressBar(self)             # Criando uma barra de progresso
        self.LayoutConversao.addWidget(self.pbar)        # Adicionando a barra de progresso no layout do widget
        self.timer = QtCore.QBasicTimer()                # Criando o objeto tempo
        self.step = 0                                    # Controlador do tempo
        self.inicio = 0                                  # Controla o relogio

    def start_conversor(self):
        if self.LEditArqOrig.text() != '' and self.LEditArqDes.text() != '':
            self.BtnConverter.setEnabled(False)
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]')+ " Convertendo arquivo...\n")
            self.CxTexto.moveCursor(QtGui.QTextCursor.End)
            self.dadosArquivo = []
            self.th = ThConversor(self.dadosArquivo, self.nome_arquivoOrigem)
            self.th.start()
            self.creat_progress_bar()
            self.doAction()
        else:
            reply = QtGui.QMessageBox.critical(self, 'Aviso', "Insira arquivos válidos", QtGui.QMessageBox.Ok)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]')+ " Conversão concluida com sucesso...\n")
            self.CxTexto.insertPlainText(strftime('[%H:%M:%S]')+ " Salvando arquivo...\n")
            SalvaArquivo(self.nome_arquivoDestino, self.dadosArquivo, self)

        if self.dadosArquivo != []:
            if (len(self.dadosArquivo)-1) <= self.dadosArquivo[0]:
                 self.step = ((len(self.dadosArquivo)-1)*100)//self.dadosArquivo[0]
                 self.pbar.setValue(self.step)
            self.inicio = self.inicio + 0.1

    def doAction(self):
        self.timer.isActive()
        self.timer.start(100, self)

    def arqOrigem(self):
        reply = QtGui.QMessageBox.information(self, 'Aviso', "Por favor insira o arquivo xlsx pra conversão", QtGui.QMessageBox.Ok)
        self.nome_arquivoOrigem = QtGui.QFileDialog.getOpenFileName(self, "Selecionar o arquivo xlsx", filter="All(*.xlsx)")  ##Abre um arquivo
        self.LEditArqOrig.setText(self.nome_arquivoOrigem)

    def arqDestino(self):
        reply = QtGui.QMessageBox.information(self,'Aviso',"Selecione a pasta para salvar o arquivo", QtGui.QMessageBox.Ok)
        self.nome_arquivoDestino = QtGui.QFileDialog.getSaveFileName(self, "Selecionar o local para salvar o arquivo", filter="All(*.txt)")  ##Abre um arquivo
        self.LEditArqDes.setText(self.nome_arquivoDestino)

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