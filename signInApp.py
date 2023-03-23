from PyQt5 import QtWidgets
from sign_in_ui import Ui_MainWindow
import sys


class sign_in(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(sign_in, self).__init__()
        self.setupUi(self)
        self.button = QtWidgets.QPushButton("Click me")
        self.label = QtWidgets.QLabel()
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Connect the clicked signal to a slot function
        self.button.clicked.connect(self.handle_click)

    def handle_click(self):
        self.label.setText("Button clicked")

    def get_admin(self):
        cur, conn = db_connect.get_connection()
        print(cur, conn)
        # Execute a query
        cur.execute("SELECT * FROM staff")
        # Fetch the results
        results = cur.fetchall()
        # Print the results
        for row in results:
            print(row[2])
            user = row[1]
            password = row[2]

    def inputs(self):
        u = self.lineEdit.text()
        ue = self.lineEdit_2.text()
        print(u, ue)


if __name__ == "__main__":
    import sys

    # app = QtWidgets.QApplication(sys.argv)
    # form = sign_in()
    # Ui_MainWindow().setupUi(form)
    # form.show()
    # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
