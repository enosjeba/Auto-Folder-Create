from PyQt5 import QtCore, QtGui, QtWidgets
from FolderList import Ui_FolderName
import os


class Ui_MainWindow(object):
    def OpenWindow(self):
        
        #Create Folder
        name = self.lineEdit.text()
        os.mkdir(f'./{name}/')
        os.chdir(f'./{name}')

        #open second window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FolderName()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 207)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 361, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.OpenWindow())
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 121, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 26))
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
        self.label.setText(_translate("MainWindow", "Enter your Project Name"))
        self.pushButton.setText(_translate("MainWindow", "Create Project"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())