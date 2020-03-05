from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget


class AdvancedSettingsWidget(QWidget):

    def __init__(self):
        _translate = QtCore.QCoreApplication.translate
        super().__init__()
        self.gridLayout = QtWidgets.QGridLayout()
        self.neuron_counter_label = QtWidgets.QLabel()
        self.neuron_counter_line = QtWidgets.QLineEdit()
        self.activation_func_label = QtWidgets.QLabel()
        self.activation_func_cmb = QtWidgets.QComboBox()
        self.kernel_init_label = QtWidgets.QLabel()
        self.kernel_init_cmb = QtWidgets.QComboBox()
        self.setWindowTitle(_translate("AdvancedWgt", "AdvancedWgt"))
        self.neuron_counter_label.setText("Количество нейронов в слое: ")
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

    # def initUi(self,i):
    #     lbl1 = QtWidgets.QLabel()
    #     le1 = QtWidgets.QLineEdit()
    #     lbl2 = QtWidgets.QLabel()
    #     cmb1 = QtWidgets.QComboBox()
    #     lbl3 = QtWidgets.QLabel()
    #     cmb2 = QtWidgets.QComboBox()
    #
    #     lbl1.setText("Количество нейронов в слое: ")
    #     cmb1.setItemText(0, "RELU")
    #     cmb1.setItemText(1, "Sigmoid")
    #     cmb1.setItemText(2, "ELU")
    #     cmb1.setItemText(3, "Tangh")
    #     cmb1.setItemText(4, "Softmax")
    #     lbl2.setText("Функция активации: ")
    #     lbl3.setText("Способ инициализации весов: ")
    #     cmb2.setItemText(0, "Zeros")
    #     cmb2.setItemText(1, "Ones")
    #     cmb2.setItemText(2, "RandomNormal")
    #     cmb2.setItemText(3, "RandomUniform")
    #     cmb2.setItemText(4, "TruncatedNormal")
    #     cmb2.setItemText(5, "Lecun_uniform")
    #     cmb2.setItemText(6, "He_normal")
    #     cmb2.setItemText(7, "Lecun_normal")
    #     cmb2.setItemText(8, "He_uniform")
    #     cmb2.setItemText(9, "SVD")
    #     # self.neuron_counter_label.append(lbl1)
    #     # self.neuron_counter_line.append(le1)
    #     # self.activation_func_label.append(lbl2)
    #     # self.activation_func_cmb.append(cmb1)
    #     # self.kernel_init_label.append(lbl3)
    #     # self.kernel_init_cmb.append(cmb2)
    #     # self.neuron_counter_label[i].setText("Количество нейронов в" + i + " слое: ")
    #     # self.activation_func_cmb[i].setItemText(0, "RELU")
    #     # self.activation_func_cmb[i].setItemText(1, "Sigmoid")
    #     # self.activation_func_cmb[i].setItemText(2, "ELU")
    #     # self.activation_func_cmb[i].setItemText(3, "Tangh")
    #     # self.activation_func_cmb[i].setItemText(4, "Softmax")
    #     # self.activation_func_label[i].setText("Функция активации: ")
    #     # self.kernel_init_label[i].setText("Способ инициализации весов: ")
    #     # self.kernel_init_cmb[i].setItemText(0, "Zeros")
    #     # self.kernel_init_cmb[i].setItemText(1, "Ones")
    #     # self.kernel_init_cmb[i].setItemText(2, "RandomNormal")
    #     # self.kernel_init_cmb[i].setItemText(3, "RandomUniform")
    #     # self.kernel_init_cmb[i].setItemText(4, "TruncatedNormal")
    #     # self.kernel_init_cmb[i].setItemText(5, "Lecun_uniform")
    #     # self.kernel_init_cmb[i].setItemText(6, "He_normal")
    #     # self.kernel_init_cmb[i].setItemText(7, "Lecun_normal")
    #     # self.kernel_init_cmb[i].setItemText(8, "He_uniform")
    #     # self.kernel_init_cmb[i].setItemText(9, "SVD")

