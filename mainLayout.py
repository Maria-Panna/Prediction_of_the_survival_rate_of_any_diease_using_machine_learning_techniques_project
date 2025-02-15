# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainframe = QtWidgets.QFrame(Dialog)
        self.mainframe.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainframe)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.mainframe)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 574, 545))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_1.setMinimumSize(QtCore.QSize(450, 480))
        self.frame_1.setMaximumSize(QtCore.QSize(16777215, 480))
        self.frame_1.setStyleSheet("border: 2px solid rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 127);\n"
"border-radius: 10px;")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_24 = QtWidgets.QLabel(self.frame_1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"  border-radius: 8px;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_1)
        self.label_10.setMinimumSize(QtCore.QSize(10, 10))
        self.label_10.setMaximumSize(QtCore.QSize(50, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: 0px;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 2, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame_1)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background: None;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 22)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 0px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(150, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 0px;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 0px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 0px;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 1, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar_3.setStyleSheet("QProgressBar{\n"
"    background: rgb(227, 227, 227);\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(212, 255, 0, 150);\n"
"    margin: 1px;\n"
"    border-radius: 8px;\n"
"}")
        self.progressBar_3.setProperty("value", 50)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_3.addWidget(self.progressBar_3, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: 0px;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0px;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar_2.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"    background: rgb(227, 227, 227);\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(77, 255, 0, 150);\n"
"    margin: 1px;\n"
"    border-radius: 8px;\n"
"}")
        self.progressBar_2.setProperty("value", 97)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_3.addWidget(self.progressBar_2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 0px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar_4.setStyleSheet("QProgressBar{\n"
"    background: rgb(227, 227, 227);\n"
"    border-radius: 8px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(255, 176, 49, 150);\n"
"    margin: 1px;\n"
"    border-radius: 8px;\n"
"}")
        self.progressBar_4.setProperty("value", 50)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_3.addWidget(self.progressBar_4, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 9, 0, 1, 5)
        self.progressBar = QtWidgets.QProgressBar(self.frame_1)
        self.progressBar.setMinimumSize(QtCore.QSize(150, 70))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(227, 227, 227); \n"
"    border-radius: 10px;  /\n"
"    text-align: center; \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 128, 0); \n"
"    margin: 1px; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        
        

        self.progressBar.setProperty("value", 20)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 7, 0, 1, 5)
        self.label_11 = QtWidgets.QLabel(self.frame_1)
        self.label_11.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: 0px;")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setMinimumSize(QtCore.QSize(100, 50))
        self.label.setMaximumSize(QtCore.QSize(450, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: None;")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_1)
        self.frame.setMinimumSize(QtCore.QSize(150, 150))
        self.frame.setMaximumSize(QtCore.QSize(150, 150))
        self.frame.setStyleSheet("border-radius: 75px;\n"
"background-image: url('./userInterface/pyqt/resources/image.png');\n" 
" border: 5px solid white; \n"
"  background-position: center;  \n"
"    background-repeat: no-repeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
        self.progressBar.raise_()
        self.frame_4.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.label_11.raise_()
        self.label_24.raise_()
        self.label_10.raise_()
        self.gridLayout.addWidget(self.frame_1, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.mainframe)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_24.setText(_translate("Dialog", "View Details"))
        self.label_10.setText(_translate("Dialog", "Day 5"))
        self.label_6.setText(_translate("Dialog", "SpO2"))
        self.label_7.setText(_translate("Dialog", ": 80%"))
        self.label_5.setText(_translate("Dialog", "Temperature"))
        self.label_8.setText(_translate("Dialog", ": 115 bpm"))
        self.label_9.setText(_translate("Dialog", ": 100\' F"))
        self.label_3.setText(_translate("Dialog", "CMR: No"))
        self.label_2.setText(_translate("Dialog", "Age: 25"))
        self.label_4.setText(_translate("Dialog", "Heart Rate"))
        self.label_11.setText(_translate("Dialog", "Survival Rate: 20%"))
        self.label.setText(_translate("Dialog", "Patient Name"))


#import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
