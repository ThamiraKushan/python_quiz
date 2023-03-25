# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from quession import QuessionAnswer
from results_window import Ui_Result


class Ui_quiz(object):

    def __init__(self):
        newObj = QuessionAnswer()

        self.data = newObj.quiz()
        self.current_question = 1
        self.checkPoint = 1
        self.GivenAnswers = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 55, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(68, 79, 116)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(510, 310, 107, 42))
        self.pushButton.setStyleSheet(
            "#pushButton{\n"
            "padding: 8px 16px;\n"
            "height: 42px;\n"
            "background: #1877F2;\n"
            "border-radius: 8px;\n"
            "color:white;\n"
            "font-size:14px;\n"
            "\n"
            "}\n"
            "\n"
            "#pushButton:hover{\n"
            "background: white;\n"
            "color: #1877F2;\n"
            "border:1px solid #1877f2;\n"
            "}\n"
            ""
        )
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 90, 32, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:black;\n" "")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(
            "background-color:#1877F2;\n" "color:white;\n" "padding:15px;\n" ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(80, 90, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:black;\n" "")
        self.label_8.setObjectName("label_8")
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_1.setGeometry(QtCore.QRect(80, 130, 100, 20))
        self.radioButton_1.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 160, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 190, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(80, 220, 100, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, self.data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# ........................
        def clicked():
            self.current_question = self.current_question+1
            # print(f"..quize...{self.current_question}")

            print(self.answer)
            self.GivenAnswers.append(self.answer)
            self.retranslateUi(MainWindow, self.data)

        self.pushButton.clicked.connect(clicked)
        # .............

    # open new window
    def Open_ResultWindow(self):

        
        self.MainWindow_R = QtWidgets.QMainWindow()
        self.ui = Ui_Result(self.GivenAnswers)
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def retranslateUi(self, MainWindow,data):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate(
            "MainWindow", "Choose the correct answer"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "QuizMaster"))

        print("before if 1 u")
        Quizlist = []

        for item in data:
            if self.current_question == item[2]:
                Quizlist.append(item)

        if len(Quizlist) > 0:
            self.answer = ''
            self.radioButton_1.setChecked(0)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(0)
            self.radioButton_4.setChecked(0)
            # ....................
            self.label_7.setText(_translate(
                "MainWindow", f"Q{Quizlist[0][2]}."))
            self.label_8.setText(_translate("MainWindow", f"{Quizlist[0][3]}"))
            self.radioButton_1.setText(_translate(
                "MainWindow", f"{Quizlist[0][6]}"))
            self.radioButton_1.toggled.connect(
                lambda: self.radio_button_selected(Quizlist[0][5]))
            self.radioButton_2.setText(_translate(
                "MainWindow", f"{Quizlist[1][6]}"))
            self.radioButton_2.toggled.connect(
                lambda: self.radio_button_selected(Quizlist[1][5]))
            self.radioButton_3.setText(_translate(
                "MainWindow", f"{Quizlist[2][6]}"))
            self.radioButton_3.toggled.connect(
                lambda: self.radio_button_selected(Quizlist[2][5]))
            self.radioButton_4.setText(_translate(
                "MainWindow", f"{Quizlist[3][6]}"))
            self.radioButton_4.toggled.connect(
                lambda: self.radio_button_selected(Quizlist[3][5]))
        else:
            self.label_7.setText(_translate("MainWindow", f"1"))
            self.label_8.setText(_translate("MainWindow", f"2"))
            self.radioButton_1.setText(_translate("MainWindow", f"3"))
            self.radioButton_2.setText(_translate("MainWindow", f"4"))
            self.radioButton_3.setText(_translate("MainWindow", f"5"))
            self.radioButton_4.setText(_translate("MainWindow", f"0"))
            # change the butto name
            self.pushButton.setText(_translate("MainWindow", "View Results"))

            self.pushButton.clicked.connect(self.Open_ResultWindow)

    def radio_button_selected(self, button):
        self.answer = button
        # print(self.answer)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_quiz()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
