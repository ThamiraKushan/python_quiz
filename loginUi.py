# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from hashlib import md5
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from connection import db_connection
from quiz_window import Ui_quiz
from file_upload import File_upload_Window
from sign_up import signup_form


class Ui_form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 429)
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("background-color: rgb(20, 79, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 90, 130, 29))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label.setMinimumSize(self.label.sizeHint())
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")

        self.label_2.setMinimumSize(self.label.sizeHint())
        # self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 251, 42))
        self.lineEdit.setStyleSheet(
            "color:black;\n"
            "padding:10px;\n"
            "background: #FFFFFF;\n"
            "border: 1px solid #D0D5DD;\n"
            "border-radius: 4px;"
        )
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 251, 42))
        self.lineEdit_2.setStyleSheet(
            "color:black;\n"
            "padding:10px;\n"
            "background: #FFFFFF;\n"
            "border: 1px solid #D0D5DD;\n"
            "border-radius: 4px;"
        )
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 162, 91, 16))
        self.label_6.setStyleSheet("color: #344054;")
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumSize(self.label.sizeHint())
        # self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 82, 91, 16))
        self.label_5.setStyleSheet("color: #344054;")
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumSize(self.label.sizeHint())
        # self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_up_link = QtWidgets.QLabel(self.frame_2)
        self.sign_up_link.setGeometry(QtCore.QRect(40, 245, 71, 16))
        self.sign_up_link.setStyleSheet(
            "#sign_up_link{color:black}\n"
            "\n"
            "#sign_up_link:hover{color:rgb(20, 79, 255);}\n"
            ""
        )
        self.sign_up_link.setObjectName("sign_up_link")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setGeometry(QtCore.QRect(40, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("color:black;")
        self.title.setObjectName("title")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 251, 48))
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
        self.label_7.setGeometry(QtCore.QRect(40, 245, 151, 16))
        self.label_7.setStyleSheet("color:rgb(68, 79, 116)")
        self.label_7.setObjectName("label_7")
        self.label_7.setMinimumSize(self.label.sizeHint())
        # self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_up_link_2 = QtWidgets.QLabel(self.frame_2)
        self.sign_up_link_2.setGeometry(QtCore.QRect(190, 245, 71, 16))
        self.sign_up_link_2.setStyleSheet(
            "#sign_up_link_2{color:black}\n"
            "#sign_up_link_2:hover{color:rgb(20, 79, 255);}\n"
            ""
        )
        self.sign_up_link_2.setObjectName("sign_up_link_2")
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.sign_up_link.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.sign_up_link_2.raise_()
        self.title.raise_()
        self.horizontalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QuizMaster"))
        self.label_2.setText(
            _translate(
                "MainWindow", "Think fast, score high. The ultimate Quiz App experience"
            )
        )
        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "Enter ID number"))
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "Enter Password"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "ID Number"))
        self.sign_up_link.setText(_translate("MainWindow", "Sign Up"))
        self.title.setText(_translate("MainWindow", "Sign in"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.label_7.setText(_translate(
            "MainWindow", "Don’t have an account?"))
        self.sign_up_link_2.setText(_translate("MainWindow", "Sign Up"))

        self.label.setMinimumSize(self.label.sizeHint())
        self.label_2.setMinimumSize(self.label_2.sizeHint())
        self.label_5.setMinimumSize(self.label_5.sizeHint())
        self.label_6.setMinimumSize(self.label_6.sizeHint())
        self.label_7.setMinimumSize(self.label_7.sizeHint())
        self.label.setWordWrap(True)
        self.label_2.setWordWrap(True)
        self.label_5.setWordWrap(True)
        self.label_6.setWordWrap(True)
        self.label_7.setWordWrap(True)

        # button clicked
        self.pushButton.clicked.connect(self.checkUser)
        self.sign_up_link_2.mousePressEvent = self.register

    # def get_admin(self):
    #     cursor = db_connection.cursor()
    #     cursor.execute("SELECT * FROM staff")
    #     # Fetch the results
    #     results = cursor.fetchall()
    #     return results

    def register(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = signup_form()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openQuiz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_quiz()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openFileUpload(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = File_upload_Window()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def checkUser(self):
        user_id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        hash_obj = hashlib.md5()
        hash_obj.update(password.encode("utf-8"))
        hash_password = hash_obj.hexdigest()
        # for user in self.get_admin():
        #     print(user)
        #     if user[1] == user_id and user[2] == hash_password:
        #         print("user exists")
        #         sys.exit(app.exec_())
        #     else:
        #         print("login faild")

        cursor = db_connection.cursor(dictionary=True)
        sql = "SELECT user_role,email FROM user WHERE user_id = %s AND password = %s;"
        cursor.execute(sql, (user_id, hash_password))
        result = cursor.fetchone()
        print(result)
        if result:
            print(result["user_role"])

        if result != [] or result != None:
            if result["user_role"] == "admin":
                print("admin")
                self.openFileUpload()
            else:
                print("student")
                self.openQuiz()
        else:
            print("failed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
