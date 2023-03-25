# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from quession import QuessionAnswer


class Ui_AnswerWindow(object):

    current_question = 0

    def __init__(self):
        self.ObjQuiz = QuessionAnswer()
        self.data = self.ObjQuiz.ViewCorrectAnswer()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 319)
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
        self.label_4.setGeometry(QtCore.QRect(400, 355, 33, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(68, 79, 116)")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(330, 210, 107, 42))
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
        self.label.setGeometry(QtCore.QRect(0, 0, 461, 49))
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
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 99, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setMinimumSize(self.label.sizeHint())
        self.label_4.setMinimumSize(self.label_4.sizeHint())
        self.label_5.setMinimumSize(self.label_5.sizeHint())
        self.label_7.setMinimumSize(self.label_7.sizeHint())
        self.label_8.setMinimumSize(self.label_8.sizeHint())
        self.label.setWordWrap(True)
        self.label_4.setWordWrap(True)
        self.label_5.setWordWrap(True)
        self.label_7.setWordWrap(True)
        self.label_8.setWordWrap(True)

        self.retranslateUi(MainWindow, self.data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def clicked():
            self.current_question = self.current_question+1
            print(f".....{self.current_question}")
            self.retranslateUi(MainWindow, self.data)
        self.pushButton.clicked.connect(clicked)

        def clicked():
            self.current_question = self.current_question + 1
            print(f"Quiz.....{self.current_question}")
            self.retranslateUi(MainWindow, self.data)

        self.pushButton.clicked.connect(clicked)

        # .............................................................

        # _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label_4.setText(_translate("MainWindow", "Correct answer"))
        # self.label.setText(_translate("MainWindow", "QuizMaster"))

        # self.pushButton.setText(_translate("MainWindow", "Next"))
        # self.label_7.setText(_translate("MainWindow", "Q"+str(i)+"."))

        # self.label_8.setText(_translate("MainWindow", "The question goes here"))
        # self.label_5.setText(_translate("MainWindow", "Correct answer"))

    # ..............................................................
    def retranslateUi(self, MainWindow, data):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Correct answer"))
        self.label.setText(_translate("MainWindow", "QuizMaster"))

        if self.current_question < len(data):
            self.pushButton.setText(_translate("MainWindow", "Next"))
            self.label_7.setText(
                _translate("MainWindow", f"{data[self.current_question][2]}")
            )

            self.label_8.setText(
                _translate("MainWindow", f"{data[self.current_question][3]}")
            )
            self.label_5.setText(
                _translate("MainWindow", f"{data[self.current_question][9]}")
            )
        else:
            self.pushButton.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AnswerWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
