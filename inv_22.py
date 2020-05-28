import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Kde_plot(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4,dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.compute_init_figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_init_figure(self):
        self.axes.plot([1,2,3,4,5,6], [4,2,6,7,2,-1])
        pass


class inv_2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setObjectName("库存决策支持系统")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 70, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_widget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.matplt = Kde_plot(self.main_widget, width=5, height=4, 
                               dpi=100)
        self.layout.addWidget(self.matplt)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inv2 = inv_2()
    inv2.show()
    sys.exit(app.exec_())