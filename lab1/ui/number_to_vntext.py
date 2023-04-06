# Form implementation generated from reading ui file 'ui/number_to_vntext.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_number_to_vntext(object):
    def setupUi(self, number_to_vntext):
        number_to_vntext.setObjectName("number_to_vntext")
        number_to_vntext.resize(635, 162)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(number_to_vntext.sizePolicy().hasHeightForWidth())
        number_to_vntext.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(number_to_vntext)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(parent=number_to_vntext)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_input = QtWidgets.QLabel(parent=number_to_vntext)
        self.lbl_input.setObjectName("lbl_input")
        self.horizontalLayout.addWidget(self.lbl_input)
        self.le_input = QtWidgets.QLineEdit(parent=number_to_vntext)
        self.le_input.setObjectName("le_input")
        self.horizontalLayout.addWidget(self.le_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_ans = QtWidgets.QLabel(parent=number_to_vntext)
        self.lbl_ans.setObjectName("lbl_ans")
        self.horizontalLayout_2.addWidget(self.lbl_ans)
        self.le_ans = QtWidgets.QLineEdit(parent=number_to_vntext)
        self.le_ans.setReadOnly(True)
        self.le_ans.setObjectName("le_ans")
        self.horizontalLayout_2.addWidget(self.le_ans)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_convert = QtWidgets.QPushButton(parent=number_to_vntext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_convert.sizePolicy().hasHeightForWidth())
        self.btn_convert.setSizePolicy(sizePolicy)
        self.btn_convert.setObjectName("btn_convert")
        self.horizontalLayout_3.addWidget(self.btn_convert)
        self.btn_clear = QtWidgets.QPushButton(parent=number_to_vntext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_3.addWidget(self.btn_clear)
        self.btn_quit = QtWidgets.QPushButton(parent=number_to_vntext)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout_3.addWidget(self.btn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(number_to_vntext)
        QtCore.QMetaObject.connectSlotsByName(number_to_vntext)

    def retranslateUi(self, number_to_vntext):
        _translate = QtCore.QCoreApplication.translate
        number_to_vntext.setWindowTitle(_translate("number_to_vntext", "Number to Vietnamese text"))
        self.lbl_title.setText(_translate("number_to_vntext", "Number to Vietnamese text"))
        self.lbl_input.setText(_translate("number_to_vntext", "Number"))
        self.lbl_ans.setText(_translate("number_to_vntext", "Answer"))
        self.btn_convert.setText(_translate("number_to_vntext", "Convert"))
        self.btn_clear.setText(_translate("number_to_vntext", "Clear"))
        self.btn_quit.setText(_translate("number_to_vntext", "Quit"))