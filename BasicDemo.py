import sys

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QIcon

class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        # setGeometry == 
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('box.png'))        

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    de = Demo()
    sys.exit(app.exec_())