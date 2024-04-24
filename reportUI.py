# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(202, 134)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(7, 10, 191, 111))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.startDateUI = QtWidgets.QDateEdit(self.layoutWidget)
        self.startDateUI.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.startDateUI.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.startDateUI.setCalendarPopup(True)
        self.startDateUI.setObjectName("startDateUI")
        self.gridLayout.addWidget(self.startDateUI, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.endDateUI = QtWidgets.QDateEdit(self.layoutWidget)
        self.endDateUI.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.endDateUI.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.endDateUI.setCalendarPopup(True)
        self.endDateUI.setObjectName("endDateUI")
        self.gridLayout.addWidget(self.endDateUI, 1, 1, 1, 2)
        self.saveButtonUI = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButtonUI.setFlat(False)
        self.saveButtonUI.setObjectName("saveButtonUI")
        self.gridLayout.addWidget(self.saveButtonUI, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.errorLabelUI = QtWidgets.QLabel(self.splitter)
        self.errorLabelUI.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.errorLabelUI.setIndent(13)
        self.errorLabelUI.setObjectName("errorLabelUI")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "StartDate"))
        self.label_2.setText(_translate("Form", "EndDate"))
        self.saveButtonUI.setText(_translate("Form", "Save Report"))
        self.errorLabelUI.setText(_translate("Form", "NoErrors"))
