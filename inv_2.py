# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inv_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 70, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 30, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_datainput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_datainput.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_datainput.setFont(font)
        self.label_datainput.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datainput.setObjectName("label_datainput")
        self.horizontalLayout_2.addWidget(self.label_datainput)
        self.label_policypre = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_policypre.setFont(font)
        self.label_policypre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_policypre.setObjectName("label_policypre")
        self.horizontalLayout_2.addWidget(self.label_policypre)
        self.label_evaluation = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_evaluation.setFont(font)
        self.label_evaluation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_evaluation.setObjectName("label_evaluation")
        self.horizontalLayout_2.addWidget(self.label_evaluation)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 200, 21))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 470, 631, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(70, 510, 631, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_datademo_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_datademo_2.sizePolicy().hasHeightForWidth())
        self.btn_datademo_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.btn_datademo_2.setFont(font)
        self.btn_datademo_2.setObjectName("btn_datademo_2")
        self.horizontalLayout_5.addWidget(self.btn_datademo_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btn_next_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_2.sizePolicy().hasHeightForWidth())
        self.btn_next_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_next_2.setFont(font)
        self.btn_next_2.setObjectName("btn_next_2")
        self.horizontalLayout_5.addWidget(self.btn_next_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.figure = Mydemo(width=5, height=4, dpi=100)
        
        # 将实例化对象self.figure1添加到垂直布局layout中
        self.lay = QtWidgets.QVBoxLayout()
        self.lay.addWidget(self.figure)
        

        # 在对象的axes和axes1画板上作图
        data = list(range(1000))
        self.figure.axes.plot(data)
        self.figure.axes1.plot(data)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_datainput.setText(_translate("MainWindow", "数据输入"))
        self.label_policypre.setText(_translate("MainWindow", "策略呈现"))
        self.label_evaluation.setText(_translate("MainWindow", "效果评估"))
        self.label.setText(_translate("MainWindow", "核密度估计曲线示例："))
        self.label_2.setText(_translate("MainWindow", "s,S 策略结果："))
        self.btn_datademo_2.setText(_translate("MainWindow", "上一步"))
        self.btn_next_2.setText(_translate("MainWindow", "下一步"))


class Mydemo(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        plt.rcParams['font.family'] = ['SimHei']    # 更换字体使中文显示正常
        plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

        # 创建绘图对象，就像matlab里创建一个新的窗口那样

        self.fig = Figure(figsize=(width, height), dpi=dpi) 

        # 紧接着在这个新的窗口加上一个子图，也就是实际画图的地方
        # 看到subplot我想你也明白，可以在这里添加多个子图，并且规定子图的位置，       
        # 方法和matlab的subplot一摸一样，为了演示我加了一个新的axes1

        self.axes = self.fig.add_subplot(2, 2, 1)
        self.axes1 = self.fig.add_subplot(2, 2, 4)

        
        # 下面这个是画新图后不保留上次的图形，但这个代码似乎有问题报错了，先注释掉
        # self.axes.hold(False) 

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)


        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self, 
                                       QtWidgets.QSizePolicy.Expanding, 
                                        QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())