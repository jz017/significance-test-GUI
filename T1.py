# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from statsmodels.stats import weightstats as stests
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 600)
    # def __init__(self):
    #     super(Ui_MainWindow, self).__init__()
        # ui_MainWindow = QtWidgets.QMainWindow()
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
        
        self.alternative_input = QtWidgets.QLabel(self.centralwidget)
        self.alternative_input.setGeometry(QtCore.QRect(260, 170, 71, 21))
        self.alternative_input.setObjectName("alternative_input")
        
        # self.alternative_input = QtWidgets.QLineEdit(self.centralwidget)
        # self.alternative_input.setGeometry(QtCore.QRect(260, 170, 71, 21))
        # self.alternative_input.setObjectName("alternative_input")
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
        self.alternative_input.setText(self.null_input.text())
    
    def start(self):
        test_list = Ui_Welcom_Window.get_EDA_V(ui)
        null_mean = float(self.null_input.text())
        ztest ,propability_value = stests.ztest(test_list, x2=None, value=null_mean)
        print(float(propability_value))
        if propability_value<0.05:
            print("Null hyphothesis rejected , Alternative hyphothesis accepted")
        else:
            print("Null hyphothesis accepted , Alternative hyphothesis rejected")
            

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
        self.alternative_input.setText(_translate("MainWindow", self.null_input.text()))
        self.more_info_label.setText(_translate("MainWindow", "Need more information:"))
        self.sigma.setText(_translate("MainWindow", "Standard deviation (population) ="))
        self.start_button.setText(_translate("MainWindow", "Start the test"))
        self.z_score_result.setText(_translate("MainWindow", "z-score = "))
        self.p_value_result.setText(_translate("MainWindow", "p-value = "))
        self.conclusion.setText(_translate("MainWindow", "Conclusion:"))
        self.result_label.setText(_translate("MainWindow", "Result:"))

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow2(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow2, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)

        df = Ui_Welcom_Window.get_df(ui)    
        col =  Ui_Welcom_Window.get_EDA_V(ui)

        df.hist(column = col)

        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        
        
        df = Ui_Welcom_Window.get_df(ui)    
        col =  Ui_Welcom_Window.get_EDA_V(ui)
        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        #df.hist(column = col)
        # t = self.get_type()
        # if t == "Boxplot":
        df.boxplot(column = col, grid = False)
        # elif t == "Histogram":
        #     df.hist(column = col)
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
    
    def set_type(self, typ):
        self.typ = typ
        
    def get_type(self):
        return self.typ
    

class Ui_Welcom_Window(object):
    def setupUi(self, Welcom_Window):
        Welcom_Window.setObjectName("Welcom_Window")
        Welcom_Window.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(Welcom_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.enter())
        self.EnterButton.setGeometry(QtCore.QRect(40, 120, 113, 32))
        self.EnterButton.setObjectName("EnterButton")
        self.FileInput = QtWidgets.QLineEdit(self.centralwidget, placeholderText = '/Users/jiawenzhao/Downloads/Book1.csv')
        self.FileInput.setGeometry(QtCore.QRect(40, 90, 313, 21))
        self.FileInput.setObjectName("FileInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 71, 16))
        self.label.setObjectName("label")
        self.col_label = QtWidgets.QLabel(self.centralwidget)
        self.col_label.setGeometry(QtCore.QRect(30, 165, 280, 16))
        self.col_label.setObjectName("col_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 165, 60, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        # self.file = self.FileInput.text()
        # self.df = pd.read_csv(self.file)
        self.empty20Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.empty20(self.df))
        self.empty20Button.setGeometry(QtCore.QRect(20, 190, 151, 32))
        self.empty20Button.setObjectName("empty20Button")
        self.delete_empty_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete0rows(self.df))
        self.delete_empty_Button.setGeometry(QtCore.QRect(180, 190, 113, 32))
        self.delete_empty_Button.setObjectName("delete_empty_Button")
        self.EDA_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Box_EDA())
        self.EDA_Button.setGeometry(QtCore.QRect(170, 230, 113, 32))
        self.EDA_Button.setObjectName("EDA_Button")
        
        
        self.EDAInput = QtWidgets.QComboBox(self.centralwidget)
        self.EDAInput.activated.connect(self.check_index)
        self.EDAInput.setGeometry(QtCore.QRect(30, 230, 113, 32))
        # self.EDAInput.addItems(['One', 'Two', 'Three', 'Four'])
        self.EDAInput.setObjectName("EDAInput")
        
        # self.EDAInput = QtWidgets.QLineEdit(self.centralwidget, placeholderText = 'EDA Variable')
        # self.EDAInput.setGeometry(QtCore.QRect(30, 230, 113, 32))
        # self.EDAInput.setObjectName("EDAInput")
        
        
        self.Hist_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Hist_EDA())
        self.Hist_Button.setGeometry(QtCore.QRect(280, 230, 113, 32))
        self.Hist_Button.setObjectName("Hist_Button")
        
        self.TEST_layout = QtWidgets.QGridLayout(self.centralwidget)
        # self.setLayout(self.TEST_layout)
        self.test_catg = "z-test"
        
        self.radiobutton = QtWidgets.QRadioButton("z-test")
        self.radiobutton.setChecked(False)
        self.radiobutton.test = "z-test"
        self.radiobutton.toggled.connect(lambda: self.onClicked("z-test"))
        self.TEST_layout.addWidget(self.radiobutton, 1, 0)
        
        self.radiobutton = QtWidgets.QRadioButton("1-sided t-test")
        self.radiobutton.setChecked(False)
        self.radiobutton.test = "1-sided t-test"
        self.radiobutton.toggled.connect(lambda: self.onClicked("1-sided t-test"))
        self.TEST_layout.addWidget(self.radiobutton, 1, 1)
        
        self.radiobutton = QtWidgets.QRadioButton("2-sided t-test")
        self.radiobutton.setChecked(False)
        self.radiobutton.test = "2-sided t-test"
        self.radiobutton.toggled.connect(lambda: self.onClicked("2-sided t-test"))
        self.TEST_layout.addWidget(self.radiobutton, 1, 2)
        # self.TEST_radio = QtWidgets.QRadioButton(self.centralwidget, clicked = lambda: self.radio_select())
        # self.TEST_radio.setGeometry(QtCore.QRect(50, 340, 113, 32))
        # self.TEST_radio.setObjectName("TEST_radio")
        self.label_condition = QtWidgets.QLabel(self.centralwidget)
        self.label_condition.setGeometry(QtCore.QRect(60, 320, 160, 16))
        self.label_condition.setText("")
        self.label_condition.setObjectName("label_condition")
        # self.condition_text = self.gettext()
        
        s = "z-test conditions \n   1. normal sample distribution or n >= 30 \n \n1-sided t-test conditions \n   1. normal sample distribution or n >= 30 \n   2. unknown variance\n \n2-sided t-test conditions \n   1. normal sample distribution or n >= 20 within each group \n   2. unknown variance"
        self.condition = QtWidgets.QScrollArea(self.centralwidget)
        self.condition_w = QtWidgets.QWidget()
        self.condition_vbox = QtWidgets.QVBoxLayout()
        object = QtWidgets.QLabel(s)
        self.condition_vbox.addWidget(object)
        self.condition_w.setLayout(self.condition_vbox)
        # self.condition.setVerticalScrollBarPolicy(QtWidgets.ScrollBarAlwaysOn)
        # self.condition.setHorizontalScrollBarPolicy(QtWidgets.ScrollBarAlwaysOff)
        # self.condition.setWidgetResizable(True)
        self.condition.setWidget(self.condition_w)

        # self.setCentralWidget(self.condition)
        self.condition.setGeometry(QtCore.QRect(50, 350, 333, 90))
        self.condition.setWindowTitle('Scroll Area Condition')
        self.condition.setObjectName("condition")
        
        self.test_condition = QtWidgets.QLabel(self.centralwidget)
        self.test_condition.setGeometry(QtCore.QRect(40, 430, 160, 16))
        self.test_condition.setText("")
        self.test_condition.setObjectName("test_condition")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.start())
        self.start_button.setGeometry(QtCore.QRect(50, 460, 131, 31))
        self.start_button.setObjectName("start_button")
        # self.dialog = Ui_MainWindow()
        
        # self.h_null = QtWidgets.QLabel(self.centralwidget)
        # self.h_null.setGeometry(QtCore.QRect(40, 460, 160, 16))
        # self.h_null.setText("")
        # self.h_null.setObjectName("h_null")
        
        # self.null_entry = QtWidgets.QLineEdit(self.centralwidget)
        # self.null_entry.setGeometry(QtCore.QRect(190, 456, 73, 21))
        # self.null_entry.setObjectName("null_entry")
        
        # self.h_alt = QtWidgets.QLabel(self.centralwidget)
        # self.h_alt.setGeometry(QtCore.QRect(40, 475, 180, 16))
        # self.h_alt.setText("")
        # self.h_alt.setObjectName("h_alt")
        
        # self.test_stat = QtWidgets.QLabel(self.centralwidget)
        # self.test_stat.setGeometry(QtCore.QRect(40, 500, 180, 16))
        # self.test_stat.setText("")
        # self.test_stat.setObjectName("test_stat")
        
        Welcom_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Welcom_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 227, 24))
        self.menubar.setObjectName("menubar")
        Welcom_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Welcom_Window)
        self.statusbar.setObjectName("statusbar")
        Welcom_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Welcom_Window)
        QtCore.QMetaObject.connectSlotsByName(Welcom_Window)
        
    def enter(self):
        self.file = self.FileInput.text()
        self.df = pd.read_csv(self.file)
        df=self.df
        cols = list(df.columns)
        self.col_label.setText("columns/variables: "+str(cols[0:]))
        self.EDAInput.addItems(cols)
        print(self.file)
        

    def empty20(self,df): #replce empty cells with 0s
        # df = pd.read_csv(file)
        #df = pd.read_csv("/Users/jiawenzhao/Downloads/Book1.csv")
        df.fillna(0, inplace = True)
        for i in list(df.columns):
            for j in range(len(df[i])):
                print(df[i][j])
        # df.to_csv("/Users/jiawenzhao/Desktop/Booknew.csv")
        
    
    def delete0rows(self, df): #drop rows with empty cells
        # df = pd.read_csv(file)
        #df = pd.read_csv("/Users/jiawenzhao/Downloads/Book1.csv")
        df.replace('', np.nan, inplace = True)
        df.dropna(inplace = True)
        for i in list(df.columns):
            for j in range(len(df[i])):
                print(df[i][j])
    
    def check_index(self):
        self.EDA_V = self.EDAInput.currentText()
        # app = QtWidgets.QApplication(sys.argv)
        # w = MainWindow()
        # app.exec_()
                
    def Box_EDA(self):
        self.EDA_V = self.EDAInput.currentText()
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow()
        self.app.exec_()
       
    def gettext(self):
        if self.test_catg == "z-test":
            return("z-test conditions \n 1. normal sample distribution or n >= 30")
        elif self.test_catg == "1-sided t-test":
            return("1-sided t-test conditions \n 1. normal sample distribution or n >= 30 \n 2. unknown variance")
        elif self.test_catg == "2-sided t-test":
            return("2-sided t-test conditions \n 1. normal sample distribution or n >= 20 within each group \n 2. unknown variance")
    
    def Hist_EDA(self):
        self.EDA_V = self.EDAInput.currentText()
        self.ap = QtWidgets.QApplication(sys.argv)
        h = MainWindow2()
        self.ap.exec_()
    
    def get_df(self):
        return self.df
    
    def get_EDA_V(self):
        return self.EDA_V
    
    def get_column(self):
        return self.df[self.EDAInput.currentText()]
    
    def start(self):

        # self.dialog.show()        
        if __name__ == "__main__":
            ui_app = QtWidgets.QApplication(sys.argv)
            zTest_MainWindow = QtWidgets.QMainWindow()
            zTest = Ui_MainWindow()
            zTest.setupUi(zTest_MainWindow)
            zTest_MainWindow.show()
            sys.exit(ui_app.exec_())
        #self.ui_appp.exec_()

    
    def onClicked(self,test):
        self.test_catg = test
        print(test)
        # self.condition_text = self.gettext()
        self.condition_text = test
        self.condition = QtWidgets.QScrollArea(self.centralwidget)
        self.condition_w = QtWidgets.QWidget()
        self.condition_vbox = QtWidgets.QVBoxLayout()
        object = QtWidgets.QLabel(self.condition_text)
        self.condition_vbox.addWidget(object)
        self.condition_w.setLayout(self.condition_vbox)
        # self.condition.setVerticalScrollBarPolicy(QtWidgets.ScrollBarAlwaysOn)
        # self.condition.setHorizontalScrollBarPolicy(QtWidgets.ScrollBarAlwaysOff)
        # self.condition.setWidgetResizable(True)
        self.condition.setWidget(self.condition_w)
        self.condition.setGeometry(QtCore.QRect(50, 380, 333, 72))
        self.condition.setWindowTitle('Scroll Area Condition')
        self.condition.setObjectName("condition")
        # self.radioButton = self.sender()
        # if self.radioButton.isChecked():
        #     print("Country is %s" % (self.radioButton.country))
            
    # def radio_select(self):
    #     if self.Boxplot_radio.isChecked():
    #         app = QtWidgets.QApplication(sys.argv)
    #         w = MainWindow()
    #         app.exec_()
        

    def retranslateUi(self, Welcom_Window):
        _translate = QtCore.QCoreApplication.translate
        Welcom_Window.setWindowTitle(_translate("Welcom_Window", "MainWindow"))
        self.EnterButton.setText(_translate("Welcom_Window", "Enter"))
        self.label.setText(_translate("Welcom_Window", "FILE PATH"))
        self.col_label.setText(_translate("Welcom_Window", "columns/variables:"))
        self.empty20Button.setText(_translate("Welcom_Window", "Fill empty cell with 0"))
        self.delete_empty_Button.setText(_translate("Welcom_Window", "Delete empty"))
        self.EDA_Button.setText(_translate("Welcom_Window", "Boxplot"))
        self.Hist_Button.setText(_translate("Welcom_Window", "Histogram"))
        self.start_button.setText(_translate("Welcom_Window", "Start"))
        self.label_condition.setText(_translate("Welcom_Window", "Check your conditions!"))
        # self.test_condition.setText(_translate("Welcom_Window", "Set Your hypothesis:"))
        # self.h_null.setText(_translate("Welcom_Window", "Null hypothesis: mean = "))
        # self.h_alt.setText(_translate("Welcom_Window", "Alternative hypothesis: mean "))
        # self.test_stat.setText(_translate("Welcom_Window", "Test Statistic: "))
        # self.TEST_radio.setText(_translate("Welcom_Window", "ztest"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Welcom_Window = QtWidgets.QMainWindow()
    ui = Ui_Welcom_Window()
    ui.setupUi(Welcom_Window)
    Welcom_Window.show()
    sys.exit(app.exec_())




# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# app.exec_()