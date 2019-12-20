# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Karthik S\Desktop\AP GUI\main_antenna_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(540, 120, 621, 22))
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(540, 190, 621, 22))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.horizontalSlider_2.setFont(font)
        self.horizontalSlider_2.setMinimum(2)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(870, 150, 61, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(920, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(540, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(910, 260, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 260, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(740, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 310, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780, 310, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 781, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 150, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 90, 491, 551))
        #self.graphicsView.setObjectName("graphicsView")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(990, 310, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(750, 80, 61, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(724, 592, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 592, 71, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(530, 340, 161, 211))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(740, 340, 161, 211))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(950, 340, 256, 211))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(940, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(1070, 220, 61, 31))
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 50, 151, 31))
        self.label_10.setMinimumSize(QtCore.QSize(151, 31))
        self.label_10.setMaximumSize(QtCore.QSize(151, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.horizontalSlider.valueChanged.connect(self.value_changed_N)
        self.horizontalSlider_2.valueChanged.connect(self.value_changed_dipole)
        
        self.radioButton.toggled.connect(lambda:self.onClicked(self.radioButton))
        self.radioButton_2.toggled.connect(lambda:self.onClicked(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda:self.onClicked(self.radioButton_3))
        
        self.pushButton.clicked.connect(self.calculate_and_plot)
        
        self.pushButton_2.clicked.connect(self.clear_all)
        
        self.lineEdit_4.returnPressed.connect(self.onClick_label)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radiation Pattern of Linear Isotropic Antennas"))
        self.label_2.setText(_translate("MainWindow", "Number of Antennas (N):"))
        self.radioButton_3.setText(_translate("MainWindow", "Scanning Array"))
        self.radioButton.setText(_translate("MainWindow", "Broadside Array"))
        self.label_4.setText(_translate("MainWindow", "Maximum Radiation (Main lobe) direction is in"))
        self.radioButton_2.setText(_translate("MainWindow", "End-fire Array"))
        self.label_6.setText(_translate("MainWindow", "Nullls"))
        self.label_7.setText(_translate("MainWindow", "Sidelobes"))
        self.label.setText(_translate("MainWindow", "Radiation Pattern of Linear Isotropic Point sources"))
        self.label_3.setText(_translate("MainWindow", "Type of dipole Antenna (lambda/x) : x ="))
        self.label_8.setText(_translate("MainWindow", "Amplitude of Sidelobes"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label_9.setText(_translate("MainWindow", "Degree"))
        self.label_10.setText(_translate("MainWindow", "Radiation Pattern"))
        
    def onClick_label(self):
        self.label_5.setText(self.lineEdit_4.text())
        global deg
        deg = int(self.label_5.text())
    
    def value_changed_N(self):
        value = str(self.horizontalSlider.value())
        self.lineEdit_2.setText(value)
    
    def value_changed_dipole(self):
        value = str(self.horizontalSlider_2.value())
        self.lineEdit_3.setText(value)
        
    def clear_all(self):
        self.label_5.clear()
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.graphicsView.clear()
        self.lineEdit_4.clear()
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
    
    def onClicked(self,button):
        
        if button.text() == "Broadside Array":
            if button.isChecked() == True:
                self.lineEdit_4.setEnabled(False)
                self.label_5.setText("90")
                global deg
                deg = 90
        if button.text() == "End-fire Array":
            if button.isChecked() == True:
                self.lineEdit_4.setEnabled(False)
                self.label_5.setText("180")
                #global deg
                deg = 180
        if button.text() == "Scanning Array":
            if button.isChecked() == True:
                self.lineEdit_4.setEnabled(True)
        
    def calculate_and_plot(self):
        
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        
        N = int(str(self.horizontalSlider.value()))
        degs = deg*np.pi/180
        freq = 1
        lamda = 3e8/freq
        d = lamda/eval(str(self.horizontalSlider_2.value()))
        dr = 2*np.pi*d/lamda
        delta = -1*dr*np.cos(degs)
        phi = np.arange(0,2*np.pi,0.01)
        sci = dr*np.cos(phi) + delta
        
        #plotting
        E = list()
        for rad in phi:
            sci = dr*np.cos(rad) + delta
            num = np.sin(N*sci/2)
            den = np.sin(sci/2)
            
            E.append(np.abs(num/den))
        '''
        plot = pg.plot()
        plot.setAspectLocked()
        
        # Add polar grid lines
        
        plot.addLine(x=0, pen=0.2)
        plot.addLine(y=0, pen=0.2)
        for r in range(2, N, 2):
            circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
            circle.setPen(pg.mkPen(0.2))
            plot.addItem(circle)
        '''    
        x = E * np.cos(phi)
        y = E * np.sin(phi)
        self.graphicsView.plot(x,y)
        
        #To find Nulls
        k = 0
        val = ((2*k*np.pi/N) - delta)/dr
        nulls = list()
        while (val <=1):
            rad = np.arccos(val)
            deg1 = rad*180/np.pi
            if deg1 == deg:
                print()
            else:
                nulls.append(deg1)
                nulls.append(180-deg1)
        
            k = k + 1
            val = ((2*k*np.pi/N) - delta)/dr
        
        k = 0
        val = ((2*k*np.pi/N) - delta)/dr
        nulls_k = list()
        while (np.abs(val) <=1):
            rad = np.arccos(val)
            deg1 = rad*180/np.pi
            if deg1 == deg:
                print()
            else:
                nulls_k.append(deg1)
                nulls_k.append(180-deg1)
        
            k = k - 1
            val = ((2*k*np.pi/N) - delta)/dr
        
        for i in nulls_k:
            nulls.append(i)
        nulls = [round(null,2) for null in nulls]
        
        new_nulls = list()
        for new_null in nulls:
            if new_null not in new_nulls:
                new_nulls.append(new_null)
                
        if self.radioButton_3.text() == "Scanning Array":
            if self.radioButton_3.isChecked() == True:
                new_nulls.remove(deg)
        
        if self.radioButton_2.text() == "End-fire Array" or self.radioButton.text() =="Broadside Array":
            if self.radioButton.isChecked() == True or self.radioButton_2.isChecked() == True:
                if deg in new_nulls:
                    new_nulls.remove(deg)
                if (180-deg) in new_nulls:
                    new_nulls.remove(180-deg)
                
        
        #To find Sidelobes
        k = 0
        val = (((2*k + 1)*np.pi/N) - delta)/dr
        sidelobe = list()
        while (val <=1):
            rad = np.arccos(val)
            deg1 = rad*180/np.pi
            if deg1 == deg:
                print(deg1)
            else:
                sidelobe.append(deg1)
                sidelobe.append(180-deg1)
                
            k = k + 1
            val = round((((2*k + 1)*np.pi/N) - delta)/dr,2)
            
        k = 0
        val = (((2*k + 1)*np.pi/N) - delta)/dr
        sidelobe_k = list()
        while (np.abs(val) <=1):
            rad = np.arccos(val)
            deg1 = rad*180/np.pi
            if deg1 == deg:
                print(deg1)
            else:
                sidelobe_k.append(deg1)
                sidelobe_k.append(180-deg1)
                
            k = k - 1
            val = round((((2*k + 1)*np.pi/N) - delta)/dr,2)

        for i in sidelobe_k:
            sidelobe.append(i)
        sidelobe = [round(side,2) for side in sidelobe]
        sidelobe_copy = list()
        '''
        for i in sidelobe:
            if (not(i > nulls[0] and i < nulls[1])):
                sidelobe_copy.append(i)
        '''
        #sidelobe_copy = [round(sidec) for sidec in sidelobe_copy]
        new_sidelobe_copy = list()
        for new_side in sidelobe:
            if new_side not in new_sidelobe_copy:
                new_sidelobe_copy.append(new_side)
                
        sidelobe_amp = list()    
        update_sidelobe_copy = list()
        for i in new_sidelobe_copy:
            numer = np.sin(N*(dr*np.cos(i*np.pi/180) + delta)/2)
            den = np.sin((dr*np.cos(i*np.pi/180) + delta)/2)
            if (np.abs(numer/den) > N//2):
                pass
            else:
                update_sidelobe_copy.append(i)
            
        for i in update_sidelobe_copy:
            numer = np.sin(N*(dr*np.cos(i*np.pi/180) + delta)/2)
            den = np.sin((dr*np.cos(i*np.pi/180) + delta)/2)
            sidelobe_amp.append(np.abs(numer/den))
            
        
#            self.graphicsView.polar(rad,E,'.')
            
        for i in new_nulls:
            self.listWidget_2.addItem(str(i))
            
        for i in update_sidelobe_copy:
            self.listWidget.addItem(str(i))
            
        for i in sidelobe_amp:
            self.listWidget_3.addItem(str(i))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()

