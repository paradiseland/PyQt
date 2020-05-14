import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # x,y 原点为程序左上角
        # lbl1 = QLabel('Zetcode', self)
        # lbl1.move(15, 10)

        # lbl2 = QLabel('tutorials', self)
        # lbl2.move(35, 40)

        # lbl3 = QLabel('for programmers', self)
        # lbl3.move(55, 70)        

        okbtn = QPushButton('OK')
        cancelbtn = QPushButton('cancel')

        hbox = QHBoxLayout()
        # stretch() 为两个按钮增加了一些弹性空间
        hbox.addStretch(1)
        hbox.addWidget(okbtn)
        hbox.addWidget(cancelbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)





        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())