from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FolderName(object):
    def setupUi(self, FolderName):
        FolderName.setObjectName("FolderName")
        FolderName.resize(372, 428)
        self.centralwidget = QtWidgets.QWidget(FolderName)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 50, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 50, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget, clicked = lambda: self.addfolder())
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 351, 271))
        self.listWidget.setObjectName("listWidget")
        FolderName.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FolderName)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 26))
        self.menubar.setObjectName("menubar")
        FolderName.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FolderName)
        self.statusbar.setObjectName("statusbar")
        FolderName.setStatusBar(self.statusbar)

        self.retranslateUi(FolderName)
        QtCore.QMetaObject.connectSlotsByName(FolderName)
    
    def addfolder(self):
        #grab the item
        item = self.additem_lineEdit.text()

        #Add item to List
        self.m

    def retranslateUi(self, FolderName):
        _translate = QtCore.QCoreApplication.translate
        FolderName.setWindowTitle(_translate("FolderName", "MainWindow"))
        self.pushButton.setText(_translate("FolderName", "Clear All"))
        self.pushButton_2.setText(_translate("FolderName", "Delete Folder"))
        self.pushButton_3.setText(_translate("FolderName", "Add Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FolderName = QtWidgets.QMainWindow()
    ui = Ui_FolderName()
    ui.setupUi(FolderName)
    FolderName.show()
    sys.exit(app.exec_())
