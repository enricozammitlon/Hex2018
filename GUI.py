# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Hex2018/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from time import sleep

APP_NAME="Down To Bus-iness"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8(APP_NAME))
        MainWindow.resize(800, 600)
        self.colorCodes={"Type1":'blue',"Type2":'red',"Type3":'green'}
        self.counter=0
        self.lines=[]
        self.pres=[]
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(490, 0, 20, 531))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(550, 10, 121, 20))

        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(500, 30, 301, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 62, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # a figure instance to plot on
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 30, 491, 471))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.fig, self.ax = plt.subplots(nrows=0, ncols=0)

        #self.figure = Figure()
        self.canvas = FigureCanvas(self.fig)
        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)
        while(self.counter<=11):
            self.plot()
        self.widget.setLayout(layout)
        self.steps=[random.uniform(0.09,0.000001) for i in self.lines]
        self.outbound=[1 for i in self.steps]

        self.playButton = QtGui.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(260, 500, 83, 28))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.playButton.clicked.connect(self.play)

        self.pauseButton = QtGui.QPushButton(self.centralWidget)
        self.pauseButton.setGeometry(QtCore.QRect(180, 500, 83, 28))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.pauseButton.clicked.connect(self.pause)

        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(520, 60, 211, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 429))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.logOutput=[]
        for i in range(self.counter):
            self.logOutput.append(QtGui.QTextEdit(self.scrollAreaWidgetContents))
            self.logOutput[i].setGeometry(QtCore.QRect(10, 20+35*i, 181, 31))
            self.logOutput[i].append("%d"%i)
            self.logOutput[i].setReadOnly(True)
            self.logOutput[i].setLineWrapMode(QtGui.QTextEdit.NoWrap)
            font = self.logOutput[i].font()
            font.setFamily("Courier")
            font.setPointSize(10)
        self.scrollArea.setGeometry(QtCore.QRect(520, 60, 211, 431))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pause(self):
        self.playpause=2

    def play(self):
        self.playpause=1
        self.anim()

    def anim(self):
        while(self.playpause!=2):
            for route in range(len(self.lines)):
                for bus in range(len(route)):
                    step=self.steps[bus]
                    pre=self.pres[bus]
                    if(self.playpause==2):
                        return
                    if(self.outbound[bus]==1):
                        pre+=step
                    else:
                        pre-=step
                    if(pre>8):
                        self.outbound[bus]=0
                        pre=8
                    if(pre<0):
                        self.outbound[bus]=1
                        pre=0
                    self.logOutput[bus].setText("Bus %d is %2.2fkm away"%(bus,pre))
                    self.pres[bus]=pre
                    self.lines[bus].set_data([pre], [1])
                    self.canvas.draw()
                    QtCore.QCoreApplication.processEvents()

    def plot(self):
        self.counter+=1
        ''' plot some random stuff '''
        # random data
        data = [1 for i in range(9)]

        # create an axis
        self.ax = self.fig.add_subplot(12,1,self.counter)

        # discards the old graph
        self.ax.clear()
        plt.axis('off')
        # plot dataline
        self.ax.plot(data, 'g')
        self.pres.append(0)
        for currentBus in range(self.lines):
            self.lines[currentBus].append(plt.plot([0], [1], marker='o', markersize=6, color="red")[0])
        # refresh canvas
        self.canvas.draw()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate(APP_NAME, APP_NAME, None))
        self.label.setText(_translate(APP_NAME, "Bus Status", None))
        self.label_2.setText(_translate(APP_NAME, "MAP", None))
        self.playButton.setText(_translate(APP_NAME, "Play", None))
        self.pauseButton.setText(_translate(APP_NAME, "Pause", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
