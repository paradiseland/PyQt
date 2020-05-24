import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenu,
QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget,
QAction, qApp, QTextEdit)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont #for show text. tooltip
from PyQt5.QtCore import QCoreApplication # close instace




class Demo(QWidget):
    
    """
    Widget subclass
    """
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
        self.center()
        self.setWindowTitle('Icon')
        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 
            'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """
        centralize the window.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        # 主窗口框架中心点放到屏幕中心点
        qr.moveCenter(cp)
        # 主窗口左上角移动到框架左上角
        self.move(qr.topLeft())


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        # 创建文本区域，放在qmainwindow中间，占满所有剩余区域
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.statusbar = self.statusBar()
        # self.statusbar.showMessage('Ready')
        # QAction 是菜单栏/工具栏/快捷键的动作组合
        exitAct = QAction(QIcon('box.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('exit')
        self.toolbar.addAction(exitAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        ViewMenu = menubar.addMenu('View')
        
        menubar.setNativeMenuBar(False) # set on mac to get a close apperance with windows

        
        impMenu = QMenu('Import', self)
        # File 菜单下的选项
        impAct = QAction('import mail', self)
        impMenu.addAction(impAct)

        # submenu， 作为file的子菜单
        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # 勾选菜单
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('view statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        ViewMenu.addAction(viewStatAct)

        # 右键菜单




        # bootom place: there is a status bar to play some message.
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QMainWindow')
        self.show()
    
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        """
        Set the mouse right click menu
        """
        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        
        # exec_ 显示菜单，从鼠标右键获得当前坐标
        # maptoGlobal将当前组件相对坐标转换为窗口绝对坐标  
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # de = Demo()
    qmainw = MainWindow()
    app.setWindowIcon(QIcon('box.png'))  # here app.windowicon wil be  shown at dock in MacOs.
    # 主循环
    sys.exit(app.exec_())