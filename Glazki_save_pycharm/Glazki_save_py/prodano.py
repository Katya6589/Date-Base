# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prodano.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prodano(object):
    def setupUi(self, prodano):
        prodano.setObjectName("prodano")
        prodano.resize(666, 490)
        self.tableWidget = QtWidgets.QTableWidget(prodano)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 651, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(prodano)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 80, 121, 134))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.layoutWidget1 = QtWidgets.QWidget(prodano)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 80, 234, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_9 = QtWidgets.QLabel(prodano)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 641, 31))
        self.label_9.setMinimumSize(QtCore.QSize(0, 31))
        self.label_9.setObjectName("label_9")
        self.layoutWidget_2 = QtWidgets.QWidget(prodano)
        self.layoutWidget_2.setGeometry(QtCore.QRect(510, 80, 121, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.retranslateUi(prodano)
        QtCore.QMetaObject.connectSlotsByName(prodano)

    def retranslateUi(self, prodano):
        _translate = QtCore.QCoreApplication.translate
        prodano.setWindowTitle(_translate("prodano", "Form"))
        self.pushButton.setText(_translate("prodano", "Открыть"))
        self.pushButton_2.setText(_translate("prodano", "Добавить"))
        self.pushButton_3.setText(_translate("prodano", "Удалить"))
        self.label.setText(_translate("prodano", "Артикул"))
        self.label_2.setText(_translate("prodano", "Дата изготовления "))
        self.label_3.setText(_translate("prodano", "Номер продукта"))
        self.label_4.setText(_translate("prodano", "ID_агента"))
        self.label_9.setText(_translate("prodano", "<html><head/><body><p><span style=\" font-size:24pt;\">Продано</span></p></body></html>"))
        self.pushButton_10.setText(_translate("prodano", "Найти"))