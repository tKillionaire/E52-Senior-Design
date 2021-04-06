import numpy as np
import sys
#from plot3D import plot as plt3D
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from run import runClick
from save import saveClick
from upload import uploadClick
#4 buttons upload file, new graph, save
#visuals cnc conneted/unconnected--needs to be be for new graph 


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
       
        layout = QGridLayout()      

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([10,1,2,3,4], [0,1,20, 3,40])

    
        btnLayout = QHBoxLayout()
        
        runButton = QPushButton('Run', self)
        #runButton.clicked.connect(runClick) ##fix later 
        btnLayout.addWidget(runButton)

        saveButton = QPushButton('Save', self)
        #saveButton.clicked.connect(saveClick) ##fix later 
        btnLayout.addWidget(saveButton)

        ##ADD QComboBox -dropdown menu for sizing/data collection
        uploadButton = QPushButton('Upload', self)
        # uploadButton.clicked.connect(uploadClick) ##fix later
        btnLayout.addWidget(uploadButton)
       
        combo = QComboBox()
        combo.addItems(['1/8"','1/2"','3/4"','1"'])
        btnLayout.addWidget(combo)
        
        button_master = QWidget()
        button_master.setLayout(btnLayout)
        
        layout.addWidget(button_master, 0, 4)
        layout.addWidget(sc,1,4)
        layWidget = QWidget()
        layWidget.setLayout(layout)
        self.setCentralWidget(layWidget)

if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
