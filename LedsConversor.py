# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< O que é o arquivo >

author: Cassiano Kunsch das Neves
last edited: <25/11/2015>
"""
from PyQt4.QtGui import (QApplication)
import sys
from View.Interface import AplicativoConversor

if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = AplicativoConversor()
    app.show()
    root.exec_()