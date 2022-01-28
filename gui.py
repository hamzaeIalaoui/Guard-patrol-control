from typing import Text
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
import sys
import csv

reader_references = []
control_point_ids = []
pining_dates = []
pining_hours = []


class MainWindow(QMainWindow):

    def on_resize(self):
        self.dimension = self.size()
        width, height = self.dimension.width(), self.dimension.height()

    def setup(self, width, height):
        self.setObjectName("Mainwindow")
        self.resize(width, height)
        self.setMinimumSize(900, 649)
        self.setAutoFillBackground(True)
        self.setStyleSheet("")
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.QuitButton = QtWidgets.QPushButton(self.central_widget)
        self.QuitButton.setGeometry(QtCore.QRect(900, 630, 71, 31))
        self.QuitButton.setStyleSheet("font: 63 11pt \"URW Gothic\";\n"
                                      "background-color:  rgb(55, 91, 182)")
        self.QuitButton.setObjectName("QuitButton")
        self.mainDATA_Table = QtWidgets.QTableWidget(self.central_widget)
        self.mainDATA_Table.setGeometry(QtCore.QRect(30, 30, 611, 581))
        self.mainDATA_Table.setObjectName("mainDATA_Table")
        self.mainDATA_Table.setColumnCount(4)
        self.mainDATA_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mainDATA_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainDATA_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainDATA_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainDATA_Table.setHorizontalHeaderItem(3, item)

        self.mainDATA_Table.setColumnWidth(0, 140)
        self.mainDATA_Table.setColumnWidth(1, 160)
        self.mainDATA_Table.setColumnWidth(2, 150)
        self.mainDATA_Table.setColumnWidth(3, 160)

        self.SearchingAgentGroup = QtWidgets.QGroupBox(self.central_widget)
        self.SearchingAgentGroup.setGeometry(QtCore.QRect(670, 120, 291, 71))
        self.SearchingAgentGroup.setObjectName("SearchingAgentGroup")
        self.SearchAgentTextField = QtWidgets.QLineEdit(
            self.SearchingAgentGroup)
        self.SearchAgentTextField.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.SearchAgentTextField.setObjectName("lineEdit")
        self.AgentSearchButton = QtWidgets.QPushButton(
        self.SearchingAgentGroup)
        self.AgentSearchButton.setGeometry(QtCore.QRect(190, 30, 81, 31))
        self.AgentSearchButton.setStyleSheet("font: 63 11pt \"URW Gothic\";\n"
                                             "background-color:  rgb(55, 91, 182)")
        self.AgentSearchButton.setObjectName("QuitButton_2")
        self.AlertAgentGroup = QtWidgets.QGroupBox(self.central_widget)
        self.AlertAgentGroup.setGeometry(QtCore.QRect(670, 210, 291, 391))
        self.AlertAgentGroup.setObjectName("AlertAgentGroup")
        self.Alert_TABLE = QtWidgets.QTableWidget(self.AlertAgentGroup)
        self.Alert_TABLE.setGeometry(QtCore.QRect(10, 30, 271, 351))
        self.Alert_TABLE.setObjectName("Alert_TABLE")
        self.Alert_TABLE.setColumnCount(2)
        self.Alert_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Alert_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Alert_TABLE.setHorizontalHeaderItem(1, item)

        self.Alert_TABLE.setColumnWidth(0, 145)
        self.Alert_TABLE.setColumnWidth(1, 124)

        self.CSVsettingsGROUP = QtWidgets.QGroupBox(self.central_widget)
        self.CSVsettingsGROUP.setGeometry(QtCore.QRect(670, 30, 291, 71))
        self.CSVsettingsGROUP.setObjectName("CSVsettingsGROUP")
        self.LoadCSVbutton = QtWidgets.QPushButton(self.CSVsettingsGROUP)
        self.LoadCSVbutton.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.LoadCSVbutton.setStyleSheet("font: 63 11pt \"URW Gothic\";\n"
                                         "background-color:  rgb(55, 91, 182)")
        self.LoadCSVbutton.setObjectName("QuitButton_3")
        self.DefaultTableButton = QtWidgets.QPushButton(self.CSVsettingsGROUP)
        self.DefaultTableButton.setGeometry(QtCore.QRect(140, 30, 141, 31))
        self.DefaultTableButton.setStyleSheet("font: 63 11pt \"URW Gothic\";\n"
                                              "background-color:  rgb(55, 91, 182)")
        self.DefaultTableButton.setObjectName("QuitButton_4")

        MainWindow.setCentralWidget(self, self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.QuitButton.clicked.connect(self.exit_app)
        self.LoadCSVbutton.clicked.connect(self.on_click_load_CSV)
        self.DefaultTableButton.clicked.connect(self.default_Loaded_CSV)
        self.AgentSearchButton.clicked.connect(self.search_agent)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            "MainWindow", "Systéme de gestion des rondes"))
        self.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Systéme de gestion des rondes</p></body></html>"))
        self.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p>Systéme de gestion des rondes</p><p><br/></p></body></html>"))
        self.QuitButton.setText(_translate("MainWindow", "Quitter"))
        item = self.mainDATA_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Reférence Lecteur"))
        item = self.mainDATA_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID Point de Controle"))
        item = self.mainDATA_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date de Pointage"))
        item = self.mainDATA_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Heure de Pointage"))
        self.SearchingAgentGroup.setTitle(
            _translate("MainWindow", "Chercher Agent"))
        self.AgentSearchButton.setText(_translate("MainWindow", "Chercher"))
        self.AlertAgentGroup.setTitle(
            _translate("MainWindow", "Alerts d\'agent"))
        item = self.Alert_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Point de Controle"))
        item = self.Alert_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date de Pointage"))
        self.CSVsettingsGROUP.setTitle(
            _translate("MainWindow", "Paramètres CSV"))
        self.LoadCSVbutton.setText(_translate("MainWindow", "Charger"))
        self.DefaultTableButton.setText(
            _translate("MainWindow", "Mettre par défaut"))



    def finding_and_displaying_alerts(self,target_Agent):
        self.Alert_TABLE.setRowCount(0)
        for x in range(len(reader_references)):
            if (reader_references[x]==target_Agent) and (not pining_hours[x]):
                rowCount = self.Alert_TABLE.rowCount()
                self.Alert_TABLE.insertRow(rowCount)
                self.Alert_TABLE.setItem(rowCount,0,QtWidgets.QTableWidgetItem(control_point_ids[x]))
                self.Alert_TABLE.setItem(rowCount,1,QtWidgets.QTableWidgetItem(pining_dates[x]))
 
    def on_click_load_CSV(self):
        CSVfilePath = QFileDialog.getOpenFileName(
            None, 'OpenFile', '', "CSV file (*.csv)")
        self.CSVfilePath = CSVfilePath[0]
        with open(self.CSVfilePath, mode='r', encoding='UTF8') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            header = next(readCSV)
            for column in readCSV:
                reader_reference = column[0]
                control_point_id = column[1]
                pining_date = column[2]
                pining_hour = column[3]

                reader_references.append(reader_reference)
                control_point_ids.append(control_point_id)
                pining_dates.append(pining_date)
                pining_hours.append(pining_hour)

        self.default_Loaded_CSV()
       

    def default_Loaded_CSV(self):
        row = 0
        self.mainDATA_Table.setRowCount(len(reader_references))
        for x in range(len(reader_references)):
            self.mainDATA_Table.setItem(
                row, 0, QtWidgets.QTableWidgetItem(reader_references[x]))
            self.mainDATA_Table.setItem(
                row, 1, QtWidgets.QTableWidgetItem(control_point_ids[x]))
            self.mainDATA_Table.setItem(
                row, 2, QtWidgets.QTableWidgetItem(pining_dates[x]))
            self.mainDATA_Table.setItem(
                row, 3, QtWidgets.QTableWidgetItem(pining_hours[x]))
            row += 1

    def search_agent(self):
        target_Agent = self.SearchAgentTextField.text()
        self.mainDATA_Table.setRowCount(0)
        
        for x in range(len(reader_references)):
            if reader_references[x]==target_Agent:

                   rowCount = self.mainDATA_Table.rowCount()
                   self.mainDATA_Table.insertRow(rowCount)
                   self.mainDATA_Table.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(reader_references[x]))
                   self.mainDATA_Table.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(control_point_ids[x]))
                   self.mainDATA_Table.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(pining_dates[x]))
                   self.mainDATA_Table.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(pining_hours[x]))
        self.finding_and_displaying_alerts(target_Agent)



    def popup_close(self, input):
        if input.text() == '&Yes':
            sys.exit(1)

    def closeEvent(self, event):
        self.exit_app()

    def exit_app(self):
        message = QMessageBox()
        message.setWindowTitle('Avertissement')
        message.setText('Êtes-vous sûr de vouloir quitter ?')
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)
        message.buttonClicked.connect(self.popup_close)
        x = message.exec_()
