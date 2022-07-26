# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newdatawindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(960, 650)
        main.setMinimumSize(QtCore.QSize(960, 650))
        main.setMaximumSize(QtCore.QSize(960, 650))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 519, 651, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Clockinbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Clockinbutton.setFont(font)
        self.Clockinbutton.setStyleSheet("background-color: rgb(52, 152, 219);\n"
"color: rgb(254, 255, 255);")
        self.Clockinbutton.setCheckable(True)
        self.Clockinbutton.setObjectName("Clockinbutton")
        self.horizontalLayout.addWidget(self.Clockinbutton)
        self.setimagebutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setimagebutton.setFont(font)
        self.setimagebutton.setStyleSheet("QPushButton{\n"
"background-color: rgb(52, 152, 219);\n"
"color: rgb(254, 255, 255);\n"
"border-radius: 28 px;\n"
"}")
        self.setimagebutton.setCheckable(True)
        self.setimagebutton.setObjectName("setimagebutton")
        self.horizontalLayout.addWidget(self.setimagebutton)
        self.maskborderframe = QtWidgets.QFrame(main)
        self.maskborderframe.setGeometry(QtCore.QRect(480, 0, 480, 321))
        self.maskborderframe.setStyleSheet("border:5px solid  rgb(2, 108, 203);\n"
"background-color: qlineargradient(spread:pad, x1:0.0397727, y1:0.949, x2:0.841, y2:0.159682, stop:0 rgba(1, 29, 63, 176), stop:1 rgba(2, 108, 203, 0));\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"")
        self.maskborderframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.maskborderframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.maskborderframe.setObjectName("maskborderframe")
        self.maskfram = QtWidgets.QFrame(main)
        self.maskfram.setGeometry(QtCore.QRect(410, 5, 281, 241))
        self.maskfram.setStyleSheet("background-color:none;\n"
"image: url(:/images/img2.png);")
        self.maskfram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.maskfram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.maskfram.setObjectName("maskfram")
        self.mainbgftame = QtWidgets.QFrame(main)
        self.mainbgftame.setGeometry(QtCore.QRect(0, 85, 890, 560))
        self.mainbgftame.setMinimumSize(QtCore.QSize(890, 560))
        self.mainbgftame.setMaximumSize(QtCore.QSize(890, 560))
        self.mainbgftame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.165, x2:1, y2:0.449, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(1, 29, 63, 255));\n"
"border-top-left-radius:50px;\n"
"border-bottom-right-radius:50px;")
        self.mainbgftame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbgftame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbgftame.setObjectName("mainbgftame")
        self.logoframe_2 = QtWidgets.QFrame(self.mainbgftame)
        self.logoframe_2.setGeometry(QtCore.QRect(0, -40, 231, 191))
        self.logoframe_2.setStyleSheet("image: url(:/images/face recog logo.png);\n"
"background-color:none;")
        self.logoframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoframe_2.setObjectName("logoframe_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(640, 10, 241, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(54, 120, 182);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.timelabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.timelabel.setFont(font)
        self.timelabel.setStyleSheet("background-color: rgb(54, 120, 182);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.timelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timelabel.setObjectName("timelabel")
        self.horizontalLayout_9.addWidget(self.timelabel)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.mainbgftame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(640, 80, 241, 61))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(54, 120, 182);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.datelabel = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.datelabel.setFont(font)
        self.datelabel.setStyleSheet("background-color: rgb(54, 120, 182);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.datelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datelabel.setObjectName("datelabel")
        self.horizontalLayout_10.addWidget(self.datelabel)
        self.Submitbutton = QtWidgets.QPushButton(self.mainbgftame)
        self.Submitbutton.setGeometry(QtCore.QRect(34, 500, 821, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Submitbutton.setFont(font)
        self.Submitbutton.setStyleSheet("QPushButton#Submitbutton{\n"
"border:5px ;\n"
"    background-color: rgb(2, 108, 203);\n"
"color: rgb(255, 255, 255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#Submitbutton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(52, 73, 98), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#Submitbutton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(150,123,111,255);}")
        self.Submitbutton.setCheckable(True)
        self.Submitbutton.setObjectName("Submitbutton")
        self.groupBox = QtWidgets.QGroupBox(self.mainbgftame)
        self.groupBox.setGeometry(QtCore.QRect(30, 160, 841, 331))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:none;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.setphotobutton = QtWidgets.QPushButton(self.groupBox)
        self.setphotobutton.setEnabled(True)
        self.setphotobutton.setGeometry(QtCore.QRect(20, 180, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setphotobutton.setFont(font)
        self.setphotobutton.setStyleSheet("QPushButton#setphotobutton{\n"
"border:5px ;\n"
"    background-color: rgb(2, 108, 203);\n"
"color: rgb(255, 255, 255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#setphotobutton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(52, 73, 98), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#setphotobutton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(150,123,111,255);}")
        self.setphotobutton.setCheckable(True)
        self.setphotobutton.setObjectName("setphotobutton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(510, 40, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius:none;\n"
"background-color: transparent;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 49, 67))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 40, 261, 69))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_4.addWidget(self.nameEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 98, 105, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 98, 261, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.nameEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.nameEdit_2.setObjectName("nameEdit_2")
        self.horizontalLayout_5.addWidget(self.nameEdit_2)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(480, 180, 201, 141))
        self.frame.setStyleSheet("background-image: url(:/images/ai2.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(500, -10, 361, 261))
        self.frame_2.setStyleSheet("background-image: url(:/images/abr.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.setphotobutton.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.layoutWidget.raise_()
        self.label_4.raise_()
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.maskborderframe.raise_()
        self.horizontalLayoutWidget.raise_()
        self.mainbgftame.raise_()
        self.maskfram.raise_()

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "New Employee"))
        self.Clockinbutton.setText(_translate("main", "Submit"))
        self.setimagebutton.setText(_translate("main", "Set Photo"))
        self.label_7.setText(_translate("main", "Time :"))
        self.timelabel.setText(_translate("main", "-"))
        self.label_9.setText(_translate("main", "Date :"))
        self.datelabel.setText(_translate("main", "-"))
        self.Submitbutton.setText(_translate("main", "Start Training"))
        self.groupBox.setTitle(_translate("main", "Details"))
        self.setphotobutton.setText(_translate("main", "Take Photo"))
        self.label.setText(_translate("main", "    Please enter your name and national code\n"
"    then press Take Photo and \n"
"    Until receive 100 photos please waiting ..."))
        self.label_3.setText(_translate("main", "Name :"))
        self.nameEdit.setPlaceholderText(_translate("main", "Username"))
        self.label_4.setText(_translate("main", "National Code :"))
        self.nameEdit_2.setPlaceholderText(_translate("main", "National Code"))
import recogapp_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QDialog()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
