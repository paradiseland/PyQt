# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WarehouseEnergyConsumption.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# do some modification

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(190, 160, 111, 40))
        self.buttonBox.setMaximumSize(QtCore.QSize(400, 40))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 0, 255, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 225, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(169, 290, 191, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(390, 90, 71, 16))
        self.checkBox.setTabletTracking(False)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setGeometry(QtCore.QRect(490, 90, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 130, 71, 16))
        self.checkBox_2.setTabletTracking(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_10.setGeometry(QtCore.QRect(500, 130, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_7.setBuddy(self.lineEdit_6)
        self.label_8.setBuddy(self.lineEdit_7)
        self.label_9.setBuddy(self.lineEdit_8)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.checkBox.toggled['bool'].connect(self.lineEdit_9.setVisible)
        self.checkBox_2.toggled['bool'].connect(self.lineEdit_10.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Warehouse"))
        self.comboBox.setItemText(0, _translate("MainWindow", "AS/RS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AVS/RS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Autostore"))
        self.label_2.setText(_translate("MainWindow", "number of Aisle"))
        self.label_3.setText(_translate("MainWindow", "number of tier"))
        self.label_6.setText(_translate("MainWindow", "number of bay"))
        self.label_4.setText(_translate("MainWindow", "velocity of vehicle"))
        self.label_5.setText(_translate("MainWindow", "Velocity of lift"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "姓名(&A)"))
        self.label_8.setText(_translate("MainWindow", "年龄"))
        self.label_9.setText(_translate("MainWindow", "职位"))
        self.pushButton_2.setText(_translate("MainWindow", "exit"))
        self.checkBox.setText(_translate("MainWindow", "显示/隐藏"))
        self.checkBox_2.setText(_translate("MainWindow", "显示/隐藏"))
