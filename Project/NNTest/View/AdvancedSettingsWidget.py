from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic


class AdvancedSettingsWidget(QWidget):

    def __init__(self, parent=None, i=0):
        _translate = QtCore.QCoreApplication.translate
        QWidget.__init__(self, parent=parent)
        self.gridLayout = QtWidgets.QGridLayout()
        self.neuron_counter_label = QtWidgets.QLabel()
        self.neuron_counter_line = QtWidgets.QLineEdit()
        self.activation_func_label = QtWidgets.QLabel()
        self.activation_func_cmb = QtWidgets.QComboBox()
        self.kernel_init_label = QtWidgets.QLabel()
        self.kernel_init_cmb = QtWidgets.QComboBox()
        self.i = i
        row, col = 0, 0
        self.gridLayout.addWidget(self.neuron_counter_label, row, col)
        col += 1
        self.gridLayout.addWidget(self.neuron_counter_line, row, col)
        row += 1
        col = 0
        self.gridLayout.addWidget(self.activation_func_label, row, col)
        col += 1
        self.gridLayout.addWidget(self.activation_func_cmb, row, col)
        row += 1
        col = 0
        self.gridLayout.addWidget(self.kernel_init_label, row, col)
        col += 1
        self.gridLayout.addWidget(self.kernel_init_cmb, row, col)
        row += 1
        col = 0
        self.setLayout(self.gridLayout)
        self.initUi()

    def initUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AdvancedWgt", "Конфигурация слоя"))
        self.neuron_counter_label.setText("Количество нейронов в " + str(self.i + 1) + " слое: ")
        self.activation_func_cmb.addItem("")
        self.activation_func_cmb.addItem("RELU")
        self.activation_func_cmb.addItem("Sigmoid")
        self.activation_func_cmb.addItem("ELU")
        self.activation_func_cmb.addItem("Tangh")
        self.activation_func_cmb.addItem("Softmax")
        self.activation_func_label.setText("Функция активации: ")
        self.kernel_init_label.setText("Способ инициализации весов: ")
        self.kernel_init_cmb.addItem("")
        self.kernel_init_cmb.addItem("Zeros")
        self.kernel_init_cmb.addItem("Ones")
        self.kernel_init_cmb.addItem("RandomNormal")
        self.kernel_init_cmb.addItem("RandomUniform")
        self.kernel_init_cmb.addItem("TruncatedNormal")
        self.kernel_init_cmb.addItem("Lecun_uniform")
        self.kernel_init_cmb.addItem("He_normal")
        self.kernel_init_cmb.addItem("Lecun_normal")
        self.kernel_init_cmb.addItem("He_uniform")
        self.kernel_init_cmb.addItem("SVD")

    def get_fields(self):
        return [self.neuron_counter_line.text(), self.activation_func_cmb.currentText(),
                self.kernel_init_cmb.currentText()]
