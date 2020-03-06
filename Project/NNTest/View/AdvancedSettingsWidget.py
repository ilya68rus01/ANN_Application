from PyQt5 import QtWidgets,QtCore
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

    def __init__(self,i):
        _translate = QtCore.QCoreApplication.translate
        super().__init__()
        self.gridLayout = QtWidgets.QGridLayout()
        self.neuron_counter_label = QtWidgets.QLabel()
        self.neuron_counter_line = QtWidgets.QLineEdit()
        self.activation_func_label = QtWidgets.QLabel()
        self.activation_func_cmb = QtWidgets.QComboBox()
        self.kernel_init_label = QtWidgets.QLabel()
        self.kernel_init_cmb = QtWidgets.QComboBox()
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
        self.initUi(i)

    def initUi(self,i):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AdvancedWgt", "Конфигурация слоя"))
        self.neuron_counter_label.setText("Количество нейронов в " + str(i+1) + " слое: ")
        self.activation_func_cmb.setItemText(0, _translate("AdvancedWgt", "RELU"))
        self.activation_func_cmb.setItemText(1, _translate("AdvancedWgt", "Sigmoid"))
        self.activation_func_cmb.setItemText(2, _translate("AdvancedWgt", "ELU"))
        self.activation_func_cmb.setItemText(3, _translate("AdvancedWgt", "Tangh"))
        self.activation_func_cmb.setItemText(4, _translate("AdvancedWgt", "Softmax"))
        self.activation_func_label.setText("Функция активации: ")
        self.kernel_init_label.setText("Способ инициализации весов: ")
        self.kernel_init_cmb.setItemText(0, _translate("AdvancedWgt", "Zeros"))
        self.kernel_init_cmb.setItemText(1, _translate("AdvancedWgt", "Ones"))
        self.kernel_init_cmb.setItemText(2, _translate("AdvancedWgt", "RandomNormal"))
        self.kernel_init_cmb.setItemText(3, _translate("AdvancedWgt", "RandomUniform"))
        self.kernel_init_cmb.setItemText(4, _translate("AdvancedWgt", "TruncatedNormal"))
        self.kernel_init_cmb.setItemText(5, _translate("AdvancedWgt", "Lecun_uniform"))
        self.kernel_init_cmb.setItemText(6, _translate("AdvancedWgt", "He_normal"))
        self.kernel_init_cmb.setItemText(7, _translate("AdvancedWgt", "Lecun_normal"))
        self.kernel_init_cmb.setItemText(8, _translate("AdvancedWgt", "He_uniform"))
        self.kernel_init_cmb.setItemText(9, _translate("AdvancedWgt", "SVD"))

