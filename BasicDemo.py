import sys

from PyQt5.QtWidgets import (QApplication, 
QWidget, QPushButton, QToolTip, QMessageBox)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont #for show text. tooltip
from PyQt5.QtCore import QCoreApplication # close instace




class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        """ font for tooltip"""
        # QToolTip.setFont(QFont('SansSerif', 10))

        
        """    ICON   """
        self.setWindowIcon(QIcon('box.png'))        
        """  Button   """
        button = QPushButton('Quit', self)
        """  TOOLTIP  """
        # hover on the widget for a moment, will see the tooltip
        self.setToolTip('This is a <b>Qwidiget</b> widget')
        button.setToolTip('This is a <b>QpushButton</b> widget')
        """ PUSH BUTTON TO CLOSE INSTANCE """
        button.clicked.connect(QCoreApplication.instance().quit)
        """  建议尺寸  """
        button.resize(button.sizeHint())
        
        

        # setGeometry == resize&move
        self.setGeometry(300, 300, 300, 220) # [[x, y, width, height.
        self.setWindowTitle('Icon')
        self.show()
    
    def CloseEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 
            'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    de = Demo()
    app.setWindowIcon(QIcon('box.png'))  # here app.windowicon wil be  shown at dock in MacOs.
    # 主循环
    sys.exit(app.exec_())