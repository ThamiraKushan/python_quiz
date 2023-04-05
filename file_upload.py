

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget, QTableWidget, QTableWidgetItem
from Data_storage import QuessionAnswer
from error import error_box


class File_upload_Window(object):

    def __init__(self):
        self.filepath = ''
        self.ObjQuiz = QuessionAnswer(1)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 522)
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
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        # self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit = QtWidgets.QLabel(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 251, 42))
        self.lineEdit.setStyleSheet(
            "color:black;\n"
            "padding:10px;\n"
            "background: #FFFFFF;\n"
            "border: 1px solid #D0D5DD;\n"

            "border-radius: 4px;"
        )
        # self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(40, 30, 251, 48))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("width:100%;\n" "color:black;")
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setWordWrap(False)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.title.setObjectName("title")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 251, 48))
        self.pushButton.setStyleSheet(
            "#pushButton{\n"
            "padding: 8px 16px;\n"
            "height: 42px;\n"
            "background: white;\n"
            "border-radius: 8px;\n"
            "color:#1877F2;\n"
            "font-size:14px;\n"
            "border:1px solid #1877f2;\n"
            "}\n"
            "\n"
            "#pushButton:hover{\n"
            "background: #1877F2;\n"
            "color: white;\n"
            "}\n"
            ""
        )
        self.pushButton.setObjectName("pushButton")
        self.continueBtn = QtWidgets.QPushButton(self.frame_2)
        self.continueBtn.setGeometry(QtCore.QRect(320, 170, 251, 48))
        self.continueBtn.setStyleSheet(
            "#continueBtn{\n"
            "padding: 8px 16px;\n"
            "height: 42px;\n"
            "background: #1877F2;\n"
            "border-radius: 8px;\n"
            "color:white;\n"
            "font-size:14px;\n"
            "\n"
            "}\n"
            "\n"
            "#continueBtn:hover{\n"
            "background: white;\n"
            "color: #1877F2;\n"
            "border:1px solid #1877f2;\n"
            "}\n"
            ""
        )
        self.continueBtn.setObjectName("continueBtn")
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.title.raise_()
        self.title.setGeometry(QtCore.QRect(40, 45, 668, 35))
        self.continueBtn.raise_()
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

        # this is message bar
        self.label3 = QtWidgets.QLabel(self.frame)
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color:yellow;")
        self.label3.setObjectName("label3")

        self.label3.setGeometry(QtCore.QRect(70, 240, 651, 91))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setMinimumSize(self.label.sizeHint())
        self.label_2.setMinimumSize(self.label_2.sizeHint())
        self.label.setWordWrap(True)
        self.label_2.setWordWrap(True)

        self.pushButton.clicked.connect(self.browsefiles)

    def error(self, error_msg):
        self.window = QtWidgets.QMainWindow()
        self.ui = error_box()
        self.ui.setupUi(self.window)
        self.ui.set_text(error_msg)
        self.window.show()

    def upload_File(self):
        if self.filepath != '':
            #    self.label3.setText(self._translate("MainWindow", "Loading...."))
            #
            message = self.ObjQuiz.Insert_Data(self.filepath)
            print( message)
            # self.error("Incorrect file format! Please select a correctly formatted file.")
            self.error(message)

            #    self.label3.setText(self._translate("MainWindow", "Successfully uploaded "))
        else:
            print('Please open file')
            self.error("Please select a file")

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            QWidget(), "Open File", '', 'CSV (*.csv)')
        if fname[0]:
            self.lineEdit.setText(fname[0])
            # print(fname[0])
            self.filepath = fname[0]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QuizMaster - MIT "))
        self.label_2.setText(
            _translate(
                "MainWindow", "Think fast, score high. The ultimate Quiz App experience"
            )
        )
        # self.label3.setText(_translate("MainWindow", "Successfully uploaded "))
        self.title.setText(_translate("MainWindow", "Upload a paper "))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.continueBtn.setText(_translate("MainWindow", "Upload File"))
        self.continueBtn.clicked.connect(self.upload_File)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = File_upload_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
