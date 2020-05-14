import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip

from PyQt5.QtGui import QIcon

from PyQt5.QtGui import QFont #for show text. tooltip

class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        


        # setGeometry == resize&move
        self.setGeometry(300, 300, 300, 220) # [[x, y, width, height.
        self.setWindowTitle('Icon')
        """    ICON   """
        self.setWindowIcon(QIcon('box.png'))        
        """  Button   """
        button = QPushButton('Button', self)
        """  TOOLTIP  """
        self.setToolTip('This is a <b>Qwidiget</b> widget')
        button.setToolTip('This is a <b>QpushButton</b> widget')

        
        
        
        self.show()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    de = Demo()
    app.setWindowIcon(QIcon('box.png'))  # here app.windowicon wil be  shown at dock in MacOs.
    # 主循环
    sys.exit(app.exec_())