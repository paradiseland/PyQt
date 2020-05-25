# exec_() 应用将进入主循环，主循环会监听和分发事件
# 事件源 事件 事件目标

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QHBoxLayout, QApplication, QGridLayout, QLabel)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Vertical, self)

        vbox = QHBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


    # 事件处理器被重写  
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_P:
            self.close()


class Example2(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        # 追踪事件默认没有开启， 需要手动开启
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)
    

    # Qobject 可以自定义信号 



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())