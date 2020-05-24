# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class MainPage(QMainWindow):
    def __init__(self, Dialog):
        super(MainPage, self).__init__()
        self.initUI(Dialog)

    def initUI(self, Dialog):
        Dialog.resize(650, 480)
        self.form = Dialog
        self.form.setObjectName("window")
        self.form.setStyleSheet ("background-image: url(background1.jpg)");
        self.form.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

        back = QPushButton("Back", Dialog)
        back.setGeometry(190, 210, 50, 25)
        back.clicked.connect(self.backClicked)

    def backClicked(self):
        self.form.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = MainPage(Dialog)
    ui.show()
    sys.exit(app.exec_())