#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:41:02 2022

@author: gtondl
"""


##import pandas as pd
##import glob
import sys
##import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.uic import loadUi
##from PyQt5.uic import loadUiType
##from os.path import dirname, realpath, join



class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("CHN_Gui_vers_01.ui",self)
        self.Button_calc.clicked.connect(self.calc)
        

    def calc(self):
        c = self.c_edit.text()
        h = self.h_edit.text()
        n = self.n_edit.text()
        ##import CHN_function_vers_00
       
       ## oText = CHN_function_vers_00.chn(self)
       ## oText.oxy(self)
        c = int(c)
        h = int(h)
        n = int(n)
        o = 100-(c+h+n)
        o = str(o)
        self.Oxy.setText(o)
     ## h = self.H_input
     ## n = self.N_input
     ## self.O_output = c 
       

        

     
        
  
        

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1200)
widget.setFixedHeight(1000)
widget.show()
sys.exit(app.exec_())