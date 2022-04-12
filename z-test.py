# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z-test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from statsmodels.stats import weightstats as stests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ztest_title = QtWidgets.QLabel(self.centralwidget)
        self.ztest_title.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.ztest_title.setObjectName("ztest_title")
        self.hypothesis_label = QtWidgets.QLabel(self.centralwidget)
        self.hypothesis_label.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.hypothesis_label.setObjectName("hypothesis_label")
        self.null_hypothesis_label = QtWidgets.QLabel(self.centralwidget)
        self.null_hypothesis_label.setEnabled(True)
        self.null_hypothesis_label.setGeometry(QtCore.QRect(70, 80, 121, 16))
        self.null_hypothesis_label.setObjectName("null_hypothesis_label")
        self.null_mean = QtWidgets.QLabel(self.centralwidget)
        self.null_mean.setGeometry(QtCore.QRect(100, 110, 60, 16))
        self.null_mean.setObjectName("null_mean")
        self.null_input = QtWidgets.QLineEdit(self.centralwidget)
        self.null_input.setGeometry(QtCore.QRect(150, 110, 71, 21))
        self.null_input.setObjectName("null_input")
        self.alternative_hypothesis_label = QtWidgets.QLabel(self.centralwidget)
        self.alternative_hypothesis_label.setGeometry(QtCore.QRect(70, 140, 161, 16))
        self.alternative_hypothesis_label.setObjectName("alternative_hypothesis_label")
        self.alternative_mean = QtWidgets.QLabel(self.centralwidget)
        self.alternative_mean.setGeometry(QtCore.QRect(100, 170, 41, 16))
        self.alternative_mean.setObjectName("alternative_mean")
        self.alternative_condition = QtWidgets.QComboBox(self.centralwidget)
        self.alternative_condition.activated.connect(self.check_alt_condition)
        self.alternative_condition.setGeometry(QtCore.QRect(140, 170, 111, 26))
        self.alternative_condition.setObjectName("alternative_condition")
        self.alternative_condition.addItem("")
        self.alternative_condition.addItem("")
        self.alternative_condition.addItem("")
        self.alternative_input = QtWidgets.QLineEdit(self.centralwidget)
        self.alternative_input.setGeometry(QtCore.QRect(260, 170, 71, 21))
        self.alternative_input.setObjectName("alternative_input")
        self.more_info_label = QtWidgets.QLabel(self.centralwidget)
        self.more_info_label.setGeometry(QtCore.QRect(40, 200, 161, 31))
        self.more_info_label.setObjectName("more_info_label")
        self.sigma_input = QtWidgets.QLineEdit(self.centralwidget)
        self.sigma_input.setGeometry(QtCore.QRect(260, 230, 71, 21))
        self.sigma_input.setObjectName("sigma_input")
        self.sigma = QtWidgets.QLabel(self.centralwidget)
        self.sigma.setGeometry(QtCore.QRect(50, 230, 221, 16))
        self.sigma.setObjectName("sigma")
        self.start_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.start())
        self.start_button.setGeometry(QtCore.QRect(100, 260, 131, 31))
        self.start_button.setObjectName("start_button")
        self.z_score_result = QtWidgets.QLabel(self.centralwidget)
        self.z_score_result.setGeometry(QtCore.QRect(50, 340, 81, 31))
        self.z_score_result.setObjectName("z_score_result")
        self.p_value_result = QtWidgets.QLabel(self.centralwidget)
        self.p_value_result.setGeometry(QtCore.QRect(50, 370, 81, 31))
        self.p_value_result.setObjectName("p_value_result")
        self.conclusion = QtWidgets.QLabel(self.centralwidget)
        self.conclusion.setGeometry(QtCore.QRect(50, 400, 81, 31))
        self.conclusion.setObjectName("conclusion")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(40, 310, 81, 31))
        self.result_label.setObjectName("result_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def check_alt_condition(self):
        self.alt_condition = self.alternative_condition.currentText()
    
    def start(self):
        pass
        # ztest ,propability_value = stests.ztest(dataframe['patient_bp_before'], x2=None, value=146)
        # print(float(propability_value))
        # if propability_value<0.05:
        #     print("Null hyphothesis rejected , Alternative hyphothesis accepted")
        # else:
        #     print("Null hyphothesis accepted , Alternative hyphothesis rejected")
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ztest_title.setText(_translate("MainWindow", "Z-test"))
        self.hypothesis_label.setText(_translate("MainWindow", "Hypothesis:"))
        self.null_hypothesis_label.setText(_translate("MainWindow", "Null hypothesis:"))
        self.null_mean.setText(_translate("MainWindow", "Mean ="))
        self.alternative_hypothesis_label.setText(_translate("MainWindow", "Alternative hypothesis:"))
        self.alternative_mean.setText(_translate("MainWindow", "Mean"))
        self.alternative_condition.setItemText(0, _translate("MainWindow", "not equal"))
        self.alternative_condition.setItemText(1, _translate("MainWindow", "greater than"))
        self.alternative_condition.setItemText(2, _translate("MainWindow", "less than"))
        self.more_info_label.setText(_translate("MainWindow", "Need more information:"))
        self.sigma.setText(_translate("MainWindow", "Standard deviation (population) ="))
        self.start_button.setText(_translate("MainWindow", "Start the test"))
        self.z_score_result.setText(_translate("MainWindow", "z-score = "))
        self.p_value_result.setText(_translate("MainWindow", "p-value = "))
        self.conclusion.setText(_translate("MainWindow", "Conclusion:"))
        self.result_label.setText(_translate("MainWindow", "Result:"))


if __name__ == "__main__":
# def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

