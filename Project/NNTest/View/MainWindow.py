# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import uic
from View.AdvancedSettingsWidget import *


class Ui_MainWindow():

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
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
        self.Info_Frame.setMinimumSize(QtCore.QSize(300, 650))
        self.Info_Frame.setObjectName("Info_Frame")
        self.data_tab = QtWidgets.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.Info_Frame.addTab(self.data_tab, "")
        self.struct_tab = QtWidgets.QWidget()
        self.struct_tab.setObjectName("struct_tab")
        self.Info_Frame.addTab(self.struct_tab, "")
        self.learning_tab = QtWidgets.QWidget()
        self.learning_tab.setObjectName("learning_tab")
        self.Info_Frame.addTab(self.learning_tab, "")
        self.metrics_tab = QtWidgets.QWidget()
        self.metrics_tab.setObjectName("metrics_tab")
        self.Info_Frame.addTab(self.metrics_tab, "")
        self.horizontalLayout_2.addWidget(self.Info_Frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_type_lbl = QtWidgets.QLabel(self.centralwidget)
        self.settings_type_lbl.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.settings_type_lbl.setFont(font)
        self.settings_type_lbl.setObjectName("settings_type_lbl")
        self.verticalLayout.addWidget(self.settings_type_lbl)
        self.simple_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.simple_rbtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.simple_rbtn.setFont(font)
        self.simple_rbtn.setObjectName("simple_rbtn")
        self.verticalLayout.addWidget(self.simple_rbtn)
        self.advanced_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.advanced_rbtn.setFont(font)
        self.advanced_rbtn.setObjectName("advanced_rbtn")
        self.verticalLayout.addWidget(self.advanced_rbtn)
        self.LayerCounter = QtWidgets.QGridLayout()
        self.LayerCounter.setObjectName("LayerCounter")
        self.LayerCountLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LayerCountLineEdit.setObjectName("LayerCountLineEdit")
        self.LayerCounter.addWidget(self.LayerCountLineEdit, 1, 1, 1, 1)
        self.LayerCountLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.LayerCountLabel.setFont(font)
        self.LayerCountLabel.setObjectName("LayerCountLabel")
        self.LayerCounter.addWidget(self.LayerCountLabel, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.LayerCounter)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AdvancedLayout = QtWidgets.QVBoxLayout()
        self.AdvancedLayout.setObjectName("AdvancedLayout")
        self.verticalLayout_2.addLayout(self.AdvancedLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.epoch_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.epoch_lbl.setFont(font)
        self.epoch_lbl.setObjectName("epoch_lbl")
        self.gridLayout_2.addWidget(self.epoch_lbl, 0, 0, 1, 1)
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Start_Button.setObjectName("Start_Button")
        self.gridLayout_2.addWidget(self.Start_Button, 1, 1, 1, 1)
        self.epoch_SpBox = QtWidgets.QSpinBox(self.centralwidget)
        self.epoch_SpBox.setMinimumSize(QtCore.QSize(245, 0))
        self.epoch_SpBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.epoch_SpBox.setObjectName("epoch_SpBox")
        self.gridLayout_2.addWidget(self.epoch_SpBox, 0, 1, 1, 1)
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Clear_Button.setObjectName("Clear_Button")
        self.gridLayout_2.addWidget(self.Clear_Button, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 26))
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
        self.actionSave_NN = QtWidgets.QAction(MainWindow)
        self.actionSave_NN.setObjectName("actionSave_NN")
        self.actionLoad_ANN = QtWidgets.QAction(MainWindow)
        self.actionLoad_ANN.setObjectName("actionLoad_ANN")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_NN)
        self.menuFile.addAction(self.actionLoad_ANN)
        self.menuInfo.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.retranslateUi(MainWindow)
        self.Info_Frame.setCurrentIndex(0)
        self.advanced_rbtn.toggled['bool'].connect(self.form_for_setting)
        self.simple_rbtn.setChecked(True)
        self.pen_style = QPen()
        self.pen_style.setStyle(Qt.SolidLine)
        self.pen_style.setWidth(1)
        self.pen_style.setCapStyle(Qt.RoundCap)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.training_graph_layout = QtWidgets.QVBoxLayout()
        self.training_graph_layout.addWidget(self.canvas)
        self.learning_tab.setLayout(self.training_graph_layout)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphic = QtWidgets.QGraphicsView(self.scene)
        self.ANNlayout = QtWidgets.QVBoxLayout()
        self.ANNlayout.addWidget(self.graphic)
        self.struct_tab.setLayout(self.ANNlayout)
        self.dx = 0
        self.scroll_area = QScrollArea()
        self.current_layers = "0"
        ############################################################3
        self.metrics = QtWidgets.QTableWidget()
        self.metrics_layout = QVBoxLayout()
        self.metrics_layout.addWidget(self.metrics)
        self.metrics_tab.setLayout(self.metrics_layout)
        self.metrics.setRowCount(3)
        self.metrics.setColumnCount(5)
        self.metrics.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #############################################################3
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Что-то вроде слота для создания виджета с настройкой структуры НС
    def form_for_setting(self):
        if self.AdvancedLayout.isEmpty() or not (int(self.LayerCountLineEdit.text()) == int(self.current_layers)):
            self.current_layers = self.LayerCountLineEdit.text()
            self.layer_list = list()
            self.scroll_area.clearFocus()
            scroll_layout = QVBoxLayout()
            wgt1 = QWidget()
            for i in range(int(self.LayerCountLineEdit.text())):
                wgt = AdvancedSettingsWidget(self.centralwidget, i)
                self.layer_list.append(wgt)
                scroll_layout.addWidget(self.layer_list[i])
            wgt1.setLayout(scroll_layout)
            self.scroll_area.setWidget(wgt1)
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            self.AdvancedLayout.addWidget(self.scroll_area)

    # Метод для отображения метрик
    def write_metrics(self):

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
        neuron_in_layer = list()  # Массив количества нейронов в слоях
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
                elif y_circle <= 0:
                    y_circle = y_circle * -1
                    y_circle += 40
            x_circle += 300
            y_circle = 0
        line.setLine(15, 15, 300, 15)
        color_positive = QColor(255, 0, 0)
        color_negative = QColor(0, 0, 255)
        print(weights[1][0])
        for i in range(np.size(neuron_in_layer) - 1):  # для количества слоев -1
            for j in range(neuron_in_layer[i]):  # для киоличества нейронов в слое
                for k in range(neuron_in_layer[i + 1]):
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
                    if line.y2() > 15:
                        line.setLine(line.x1(), line.y1(), line.x2(), line.y2() * -1 + 30)
                    elif line.y2() < 15:
                        line.setLine(line.x1(), line.y1(), line.x2(), line.y2() * -1 + 70)
                    elif line.y2() == 15:
                        line.setLine(line.x1(), line.y1(), line.x2(), line.y2() + 40)
                line.setLine(line.x1(), line.y1(), line.x2(), 15)
                if line.y1() > 15:
                    line.setLine(line.x1(), line.y1() * -1 + 30, line.x2(), line.y2())
                elif line.y1() < 15:
                    line.setLine(line.x1(), line.y1() * -1 + 70, line.x2(), line.y2())
                elif line.y1() == 15:
                    line.setLine(line.x1(), line.y1() + 40, line.x2(), line.y2())
            line.setLine(line.x1() + 300, 15, line.x2() + 300, line.y2())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.data_tab), _translate("MainWindow", "Данные"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.struct_tab),
                                   _translate("MainWindow", "Построенная ИНС"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.learning_tab),
                                   _translate("MainWindow", "График обучения"))
        self.Info_Frame.setTabText(self.Info_Frame.indexOf(self.metrics_tab), _translate("MainWindow", "Метрики"))
        self.settings_type_lbl.setText(_translate("MainWindow", "Выберите способ настройки нейронной сети: "))
        self.simple_rbtn.setText(_translate("MainWindow", "Простой"))
        self.advanced_rbtn.setText(_translate("MainWindow", "Расширенный"))
        self.LayerCountLabel.setText(_translate("MainWindow", "Количество слоев в нейронной сети:"))
        self.epoch_lbl.setText(_translate("MainWindow", "Количество эпох обучения:"))
        self.Start_Button.setText(_translate("MainWindow", "Начать"))
        self.Clear_Button.setText(_translate("MainWindow", "Сбросить"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionOpen.setText(_translate("MainWindow", "Load dataset"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.action_2.setText(_translate("MainWindow", "Создал Хрущев Илья"))
        self.actionSave_NN.setText(_translate("MainWindow", "Save ANN"))
        self.actionLoad_ANN.setText(_translate("MainWindow", "Load ANN "))
