# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic
from View.AdvancedSettingsWidget import *


class Ui_MainWindow():
    def __init__(self,MainWindow):
    # def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 697)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Info_Frame = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Info_Frame.sizePolicy().hasHeightForWidth())
        self.Info_Frame.setSizePolicy(sizePolicy)
        self.Info_Frame.setObjectName("Info_Frame")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Info_Frame.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Info_Frame.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Info_Frame.addTab(self.tab_3, "")
        self.horizontalLayout_2.addWidget(self.Info_Frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.AdvancedMode_rbttn = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.AdvancedMode_rbttn.setFont(font)
        self.AdvancedMode_rbttn.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.AdvancedMode_rbttn)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AdvancedLayout = QtWidgets.QVBoxLayout()
        self.AdvancedLayout.setObjectName("AdvancedLayout")
        self.LayerCounter = QtWidgets.QGridLayout()
        self.LayerCounter.setObjectName("LayerCounter")
        self.LayerCountLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.LayerCountLabel.setFont(font)
        self.LayerCountLabel.setObjectName("LayerCountLabel")
        self.LayerCounter.addWidget(self.LayerCountLabel, 1, 0, 1, 1)
        self.LayerCountLineEdit = QtWidgets.QLineEdit(self.frame)
        self.LayerCountLineEdit.setObjectName("LayerCountLineEdit")
        self.LayerCounter.addWidget(self.LayerCountLineEdit, 1, 1, 1, 1)
        self.AdvancedLayout.addLayout(self.LayerCounter)
        self.AdvancedModeWidget = QtWidgets.QWidget(self.frame)
        self.AdvancedModeWidget.setVisible(False)
        self.AdvancedModeWidget.setObjectName("AdvancedModeWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.AdvancedModeWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.activation_func_CBox = QtWidgets.QComboBox(self.AdvancedModeWidget)
        self.activation_func_CBox.setObjectName("activation_func_CBox")
        self.activation_func_CBox.addItem("")
        self.activation_func_CBox.addItem("")
        self.activation_func_CBox.addItem("")
        self.activation_func_CBox.addItem("")
        self.activation_func_CBox.addItem("")
        self.gridLayout.addWidget(self.activation_func_CBox, 2, 3, 1, 1)
        self.neuron_counter_SpBox = QtWidgets.QSpinBox(self.AdvancedModeWidget)
        self.neuron_counter_SpBox.setObjectName("neuron_counter_SpBox")
        self.gridLayout.addWidget(self.neuron_counter_SpBox, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.AdvancedModeWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.AdvancedModeWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.AdvancedModeWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.inizializer_CBox = QtWidgets.QComboBox(self.AdvancedModeWidget)
        self.inizializer_CBox.setObjectName("inizializer_CBox")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.inizializer_CBox.addItem("")
        self.gridLayout.addWidget(self.inizializer_CBox, 3, 3, 1, 1)
        self.AdvancedLayout.addWidget(self.AdvancedModeWidget)
        self.verticalLayout_2.addLayout(self.AdvancedLayout)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.epoch_SpBox = QtWidgets.QSpinBox(self.centralwidget)
        self.epoch_SpBox.setMinimumSize(QtCore.QSize(245, 0))
        self.epoch_SpBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.epoch_SpBox.setObjectName("epoch_SpBox")
        self.gridLayout_2.addWidget(self.epoch_SpBox, 0, 1, 1, 1)
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Clear_Button.setObjectName("Clear_Button")
        self.gridLayout_2.addWidget(self.Clear_Button, 1, 0, 1, 1)
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Start_Button.setObjectName("Start_Button")
        self.gridLayout_2.addWidget(self.Start_Button, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuInfo.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.retranslateUi(MainWindow)
        self.Info_Frame.setCurrentIndex(0)
        self.AdvancedMode_rbttn.toggled['bool'].connect(self.form_for_setting)
        self.radioButton_2.setChecked(True)
        self.pen_style = QPen()
        self.pen_style.setStyle(Qt.SolidLine)
        self.pen_style.setWidth(1)
        self.pen_style.setCapStyle(Qt.RoundCap)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.training_graph_layout = QtWidgets.QVBoxLayout()
        self.training_graph_layout.addWidget(self.canvas)
        self.tab_3.setLayout(self.training_graph_layout)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphic = QtWidgets.QGraphicsView(self.scene)
        self.ANNlayout = QtWidgets.QVBoxLayout()
        self.ANNlayout.addWidget(self.graphic)
        self.tab_2.setLayout(self.ANNlayout)
        self.dx = 0
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def form_for_setting(self):
        for i in range(int(self.LayerCountLineEdit.text())):
            self.wgt = AdvancedSettingsWidget(i)
            # self.wgt.show()
            self.AdvancedLayout.addWidget(self.wgt)
        # self.AdvancedLayout.addWidget(self.settings)

    # Метод для построения графика обучения
    def plot_history(self, data_loss, data_acc):
        # data = [np.random.random() for i in range(10)]
        print(data_loss)
        print(data_acc)
        # instead of ax.hold(False)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data_loss, '*-')
        ax.plot(data_acc, '.-g')
        # refresh canvas
        self.canvas.draw()

    # Метод для визуализации структуры и весовых коэфициентов ИНС
    def draw_model(self, weights):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphic.setScene(self.scene)
        line = QtCore.QLineF()
        neuron_in_layer = list() #Массив количества нейронов в слоях
        neuron_in_layer.append(weights[0][0].shape[0])
        for x in weights:
            neuron_in_layer.append(x[0].shape[1])
            # возвращает количество нейронов во входном слое
        x_circle = 0
        y_circle = 0
        diameter = 30
        for i in range(np.size(neuron_in_layer)):
            for j in range(neuron_in_layer[i]):
                self.scene.addEllipse(x_circle, y_circle, diameter, diameter)
                if y_circle > 0:
                    y_circle = y_circle * -1
                else:
                    y_circle = y_circle * -1
                    y_circle += 40
            x_circle += 300
            y_circle = 0
        # x1_line = 15
        # y1_line = 0
        # x2_line = 300
        # y2_line = 0
        line.setLine(15,15, 300, 15)
        color_positive = QColor(255, 0, 0)
        color_negative = QColor(0, 0, 255)
        print(weights[1][0])
        for i in range(np.size(neuron_in_layer) - 1):  # для количества слоев -1
            for j in range(neuron_in_layer[i]):  # для киоличества нейронов в слое
                for k in range(neuron_in_layer[i + 1]):
                    # print(weights[i][0][j][k])
                    if weights[i][0][j][k] > 0:
                        color_positive.setAlphaF(weights[i][0][j][k])
                        self.pen_style.setColor(color_positive)
                        self.pen_style.setWidth(int(weights[i][0][j][k] * (5 - 1) + 1))
                    elif weights[i][0][j][k] <= 0:
                        self.pen_style.setWidth(1)
                        color_negative.setAlphaF(weights[i][0][j][k] * -1)
                        self.pen_style.setColor(color_negative)
                        self.pen_style.setWidth(int(weights[i][0][j][k] * -1 * (5 - 1) + 1))
                    self.scene.addLine(line, pen=self.pen_style)
                    if line.y2() > 0:
                        line.setLine(line.x1(), line.y1(), line.x2(), line.y2() * -1 - 15)
                    else:
                        line.setLine(line.x1(), line.y1(), line.x2(), line.y2() * -1 + 40 - 15)
                        # y2_line += 40
                line.setLine(line.x1(), line.y1() - 15, line.x2(), 15)
                if line.y1() > 0:
                    line.setLine(line.x1(), line.y1() * -1 + 15, line.x2(), line.y2())
                else:
                    line.setLine(line.x1(), line.y1() * -1 + 40 + 15, line.x2(), line.y2())
                    # y1_line += 40
            # x1_line += 300
            # x2_line += 300
            # y1_line = 0
            line.setLine(line.x1() + 300, 15, line.x2() + 300, line.y2())
        # TODO реализовать визуализацию структуры ИНС

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.tab), _translate("MainWindow", "Данные"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.tab_2), _translate("MainWindow", "Структура ИНС"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.tab_3), _translate("MainWindow", "График обучения"))
        self.label.setText(_translate("MainWindow", "Выберите способ настройки нейронной сети: "))
        self.radioButton_2.setText(_translate("MainWindow", "Простой"))
        self.AdvancedMode_rbttn.setText(_translate("MainWindow", "Расширенный"))
        self.LayerCountLabel.setText(_translate("MainWindow", "Количество слоев в нейронной сети:"))
        self.activation_func_CBox.setItemText(0, _translate("MainWindow", "RELU"))
        self.activation_func_CBox.setItemText(1, _translate("MainWindow", "Sigmoid"))
        self.activation_func_CBox.setItemText(2, _translate("MainWindow", "ELU"))
        self.activation_func_CBox.setItemText(3, _translate("MainWindow", "Tangh"))
        self.activation_func_CBox.setItemText(4, _translate("MainWindow", "Softmax"))
        self.label_2.setText(_translate("MainWindow", "Количество нейронов в 1 слое:"))
        self.label_3.setText(_translate("MainWindow", "Функция активации: "))
        self.label_5.setText(_translate("MainWindow", "Метод инициализации весов"))
        self.inizializer_CBox.setItemText(0, _translate("MainWindow", "Zeros"))
        self.inizializer_CBox.setItemText(1, _translate("MainWindow", "Ones"))
        self.inizializer_CBox.setItemText(2, _translate("MainWindow", "RandomNormal"))
        self.inizializer_CBox.setItemText(3, _translate("MainWindow", "RandomUniform"))
        self.inizializer_CBox.setItemText(4, _translate("MainWindow", "TruncatedNormal"))
        self.inizializer_CBox.setItemText(5, _translate("MainWindow", "Lecun_uniform"))
        self.inizializer_CBox.setItemText(6, _translate("MainWindow", "He_normal"))
        self.inizializer_CBox.setItemText(7, _translate("MainWindow", "Lecun_normal"))
        self.inizializer_CBox.setItemText(8, _translate("MainWindow", "He_uniform"))
        self.inizializer_CBox.setItemText(9, _translate("MainWindow", "SVD"))
        self.label_4.setText(_translate("MainWindow", "Количество эпох обучения:"))
        self.Clear_Button.setText(_translate("MainWindow", "Сбросить"))
        self.Start_Button.setText(_translate("MainWindow", "Начать"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.action_2.setText(_translate("MainWindow", "Создал Хрущев Илья"))
