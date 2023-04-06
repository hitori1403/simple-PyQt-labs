# Form implementation generated from reading ui file 'ui/grade_management.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_grade_management(object):
    def setupUi(self, grade_management):
        grade_management.setObjectName("grade_management")
        grade_management.resize(1026, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(grade_management.sizePolicy().hasHeightForWidth())
        grade_management.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(grade_management)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(parent=grade_management)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_grade_list = QtWidgets.QLabel(parent=grade_management)
        self.lbl_grade_list.setObjectName("lbl_grade_list")
        self.horizontalLayout_8.addWidget(self.lbl_grade_list)
        self.le_grade_list = QtWidgets.QLineEdit(parent=grade_management)
        self.le_grade_list.setObjectName("le_grade_list")
        self.horizontalLayout_8.addWidget(self.le_grade_list)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.btn_calculate = QtWidgets.QPushButton(parent=grade_management)
        self.btn_calculate.setObjectName("btn_calculate")
        self.horizontalLayout_9.addWidget(self.btn_calculate)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.gb_list_subjects_grades = QtWidgets.QGroupBox(parent=grade_management)
        self.gb_list_subjects_grades.setObjectName("gb_list_subjects_grades")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gb_list_subjects_grades)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(958, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 121, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 1)
        self.gb_gridlayout_main = QtWidgets.QGridLayout()
        self.gb_gridlayout_main.setObjectName("gb_gridlayout_main")
        self.gridLayout_4.addLayout(self.gb_gridlayout_main, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gb_list_subjects_grades)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=grade_management)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lbl_apc = QtWidgets.QLabel(parent=grade_management)
        self.lbl_apc.setText("")
        self.lbl_apc.setObjectName("lbl_apc")
        self.horizontalLayout_3.addWidget(self.lbl_apc)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(parent=grade_management)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.lbl_gpa = QtWidgets.QLabel(parent=grade_management)
        self.lbl_gpa.setText("")
        self.lbl_gpa.setObjectName("lbl_gpa")
        self.horizontalLayout_2.addWidget(self.lbl_gpa)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=grade_management)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.lbl_hg = QtWidgets.QLabel(parent=grade_management)
        self.lbl_hg.setText("")
        self.lbl_hg.setObjectName("lbl_hg")
        self.horizontalLayout_5.addWidget(self.lbl_hg)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(parent=grade_management)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lbl_ncnp = QtWidgets.QLabel(parent=grade_management)
        self.lbl_ncnp.setText("")
        self.lbl_ncnp.setObjectName("lbl_ncnp")
        self.horizontalLayout_7.addWidget(self.lbl_ncnp)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(parent=grade_management)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lbl_lg = QtWidgets.QLabel(parent=grade_management)
        self.lbl_lg.setText("")
        self.lbl_lg.setObjectName("lbl_lg")
        self.horizontalLayout_6.addWidget(self.lbl_lg)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=grade_management)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbl_ncp = QtWidgets.QLabel(parent=grade_management)
        self.lbl_ncp.setText("")
        self.lbl_ncp.setObjectName("lbl_ncp")
        self.horizontalLayout.addWidget(self.lbl_ncp)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(grade_management)
        QtCore.QMetaObject.connectSlotsByName(grade_management)

    def retranslateUi(self, grade_management):
        _translate = QtCore.QCoreApplication.translate
        grade_management.setWindowTitle(_translate("grade_management", "Grade management"))
        self.lbl_title.setText(_translate("grade_management", "Grade management"))
        self.lbl_grade_list.setText(_translate("grade_management", "Grade list"))
        self.btn_calculate.setText(_translate("grade_management", "Calculate"))
        self.gb_list_subjects_grades.setTitle(_translate("grade_management", "List of courses and grades"))
        self.label_5.setText(_translate("grade_management", "Academic performance classification:"))
        self.label_15.setText(_translate("grade_management", "Grade point average:"))
        self.label_9.setText(_translate("grade_management", "Highest grade:"))
        self.label_13.setText(_translate("grade_management", "Number of courses not passed:"))
        self.label_11.setText(_translate("grade_management", "Lowest grade:"))
        self.label.setText(_translate("grade_management", "Number of courses passed:"))