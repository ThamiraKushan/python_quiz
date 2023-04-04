# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Data_storage import QuessionAnswer
from results_window import Ui_Result
from Bussiness_Logic import Quiz_bl
from quiz_window import Ui_quiz

class Ui_Dashboard(object):

    def __init__(self,User_Id):
        self.PaperList=[]
        self.newObj = Quiz_bl(User_Id)
        self.User_Id = User_Id
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        # self.gridLayout = QtWidgets.QVBoxLayout(self.centralwidget)
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
        self.label_4.setGeometry(QtCore.QRect(40, 65, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(81, 79, 116)")
        self.label_4.setObjectName("label_4")
        
        
        

        # .......................
        
        # ..........................
        
        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 981, 45))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(
            "background-color:#1877F2;\n" "color:white;\n" "padding:15px;\n" ""
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
       
        font = QtGui.QFont()
        font.setPointSize(14)
        
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

        self.label.setMinimumSize(self.label.sizeHint())
        self.label_4.setMinimumSize(self.label_4.sizeHint())

        # self.label_8.adjustSize()
        # self.label_8.setWordWrap(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def GenerateButton(self):
        data = self.newObj.ActivePaper()
        for i in range(len(data)):
            btn = 'pushButton_'+str(i)
            self.PaperList.append(btn)
        # ........................

        for i,btn in enumerate(self.PaperList):
            self.btn = QtWidgets.QPushButton(self.frame_2)
            self.btn.setStyleSheet(
                "#btn{\n"
                "padding: 8px 16px;\n"
                "height: 42px;\n"
                "background: #1877F2;\n"
                "border-radius: 8px;\n"
                "color:white;\n"
                "font-size:14px;\n"
                "\n"
                "}\n"
                "\n"
                "#btn:hover{\n"
                "background: white;\n"
                "color: #1877F2;\n"
                "border:1px solid #1877f2;\n"
                "}\n"
                ""
            )
            self.btn.setObjectName("btn")
            # self.btn.setText(self._translate("MainWindow", "Submit"))
            self.a=btn*510
            x = (2*i+1)*150
            y = 100
            width = 200
            height = 100
            self.btn.setGeometry(QtCore.QRect(x,y,width,height))
            self.btn.setText(self._translate(f"MainWindow", str(data[i][2])))
            self.btn.clicked.connect(lambda _, i=i: self.Open_Quiz(data[i][0]))

        # .............................
    def Open_Quiz(self,papertbID):
        try:
            # MainWindow2.close()
            print(papertbID)
            if(self.newObj.IsComplted(papertbID)):
                # self.newObj.IsComplted(papertbID)
                print('You Have alredy Submit answer')
            else:
                print('hi ',papertbID)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_quiz(papertbID,self.User_Id)
                self.ui.setupUi(self.window)
                # MainWindow.hide()
                self.window.show()
        except Exception as e:
            print(f'Sorry, Cannot proceed: {str(e)}')

        

    def retranslateUi(self, MainWindow):
        
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        
       
        self.label.setText(self._translate("MainWindow", "QuizMaster - MIT "))

       
   
        
        self.GenerateButton()

        # print(self.PaperList)
        

    


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
