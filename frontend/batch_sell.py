# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/batch_sell.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_stock = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_stock.setGeometry(QtCore.QRect(290, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_stock.setFont(font)
        self.lineEdit_stock.setText("")
        self.lineEdit_stock.setObjectName("lineEdit_stock")
        self.pushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm.setGeometry(QtCore.QRect(650, 0, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 5, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_stock = QtWidgets.QLabel(self.centralwidget)
        self.label_stock.setGeometry(QtCore.QRect(20, 140, 731, 591))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_stock.setFont(font)
        self.label_stock.setText("")
        self.label_stock.setWordWrap(True)
        self.label_stock.setObjectName("label_stock")
        self.pushButton_sell = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sell.setGeometry(QtCore.QRect(280, 740, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_sell.setFont(font)
        self.pushButton_sell.setObjectName("pushButton_sell")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(110, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(650, 50, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amount.setGeometry(QtCore.QRect(330, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_amount.setFont(font)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 50, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_percent = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_percent.setGeometry(QtCore.QRect(540, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_percent.setFont(font)
        self.lineEdit_percent.setObjectName("lineEdit_percent")
        self.label.raise_()
        self.pushButton_confirm.raise_()
        self.label_2.raise_()
        self.label_stock.raise_()
        self.pushButton_sell.raise_()
        self.label_4.raise_()
        self.lineEdit_price.raise_()
        self.label_5.raise_()
        self.pushButton_delete.raise_()
        self.label_3.raise_()
        self.lineEdit_amount.raise_()
        self.label_6.raise_()
        self.lineEdit_percent.raise_()
        self.lineEdit_stock.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_confirm.clicked.connect(MainWindow.confirm)
        self.pushButton_sell.clicked.connect(MainWindow.batch_sell_start)
        self.pushButton_delete.clicked.connect(MainWindow.delete)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_confirm.setText(_translate("MainWindow", "添加"))
        self.label.setText(_translate("MainWindow", "需要卖出的股票代码"))
        self.label_2.setText(_translate("MainWindow", "计划卖出的股票代码："))
        self.pushButton_sell.setText(_translate("MainWindow", "批量卖出"))
        self.label_4.setText(_translate("MainWindow", "卖出低"))
        self.label_5.setText(_translate("MainWindow", "%"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.label_3.setText(_translate("MainWindow", "持仓        股"))
        self.label_6.setText(_translate("MainWindow", "卖出1/   仓位"))
