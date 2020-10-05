import sys
from plot3D import plot as plt3D
from PyQt5.QtWidgets import QApplication, QMainWindow
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#4 buttons upload file, new graph, save, save as 
#visuals cnc conneted/unconnected--needs to be be for new graph 

def plotData():
    plt3D()


class gui(QtWidgets, QMainWindow):
    plotData()


app = QApplication(sys.argv)

window = gui()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
