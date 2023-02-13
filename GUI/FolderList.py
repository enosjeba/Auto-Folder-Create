import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QRegExp
from PyQt5 import QRegExpValidator


class Ui_FolderName(object):

    def setupUi(self, FolderName):
        validator = QRegExpValidator(QRegExp(r'[a-z]+[A-Z]'))
        FolderName.setObjectName("FolderName")  
        FolderName.resize(372, 516)
        self.centralwidget = QtWidgets.QWidget(FolderName)
        self.centralwidget.setObjectName("centralwidget")
        self.Foldername_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Foldername_lineEdit.setGeometry(QtCore.QRect(10, 30, 351, 40))
        self.Foldername_lineEdit.setObjectName("Foldername_lineEdit")
        self.Foldername_lineEdit.setValidator(validator)
        self.Clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clearlist())
        self.Clear_pushButton.setGeometry(QtCore.QRect(250, 80, 111, 41))
        self.Clear_pushButton.setObjectName("Clear_pushButton")
        self.DeleteFolder_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.deleteFolder())
        self.DeleteFolder_pushButton_2.setGeometry(QtCore.QRect(130, 80, 111, 41))
        self.DeleteFolder_pushButton_2.setObjectName("DeleteFolder_pushButton_2")
        self.AddFolder_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.addFolder())
        self.AddFolder_pushButton_3.setGeometry(QtCore.QRect(10, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddFolder_pushButton_3.setFont(font)
        self.AddFolder_pushButton_3.setObjectName("AddFolder_pushButton_3")
        self.FolderList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.FolderList_listWidget.setGeometry(QtCore.QRect(10, 130, 351, 280))
        self.FolderList_listWidget.setObjectName("FolderList_listWidget")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.createFolder(FolderName))
        self.submit_pushButton.setGeometry(QtCore.QRect(10, 420, 351, 41))
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
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

    #Add item to List
    def addFolder(self):
        #Grab item
        item = self.Foldername_lineEdit.text()

        #Add item to List
        self.FolderList_listWidget.addItem(item)

        #clear item
        self.Foldername_lineEdit.setText("")

    def clearlist(self):    
        self.FolderList_listWidget.clear()

    def deleteFolder(self):
        #grab Column
        clicked = self.FolderList_listWidget.currentRow()
        
        #Delete Selected Row
        self.FolderList_listWidget.takeItem(clicked)

    def ListChecker(folder_list_final):
        folder_list_final = list(filter(None,folder_list_final))
        
        return folder_list_final

    def createFolder(self, second_w):

        #List for folder names pyqt format
        folder_list = []
        folder_list_final = []

        #loop throught list widget and add items
        for index in range(self.FolderList_listWidget.count()):
            folder_list.append(self.FolderList_listWidget.item(index))
        
        for item in folder_list:
            Fname = item.text()
            folder_list_final.append(Fname)
            FList = (folder_list_final)
            print(FList , "after")
            # os.mkdir(f'./{Fname}/')
            # print(f'created folder {Fname}')

        second_w.close()
        

    def retranslateUi(self, FolderName):
        _translate = QtCore.QCoreApplication.translate
        FolderName.setWindowTitle(_translate("FolderName", "Add Folder's to Project"))
        self.Clear_pushButton.setText(_translate("FolderName", "Clear List"))
        self.DeleteFolder_pushButton_2.setText(_translate("FolderName", "Delete Folder"))
        self.AddFolder_pushButton_3.setText(_translate("FolderName", "Add Folder"))
        self.submit_pushButton.setText(_translate("FolderName", "Create Folders"))
        self.label.setText(_translate("FolderName", "Enter Folder Name"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FolderName = QtWidgets.QMainWindow()
    ui = Ui_FolderName()
    ui.setupUi(FolderName)
    FolderName.show()
    sys.exit(app.exec_())
