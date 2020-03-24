from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QDir, QModelIndex
from PyQt5 import uic
import pandas as pd


class DialogFileWidget(QWidget):

    def __init__(self, parent=None, i=0):
        _translate = QtCore.QCoreApplication.translate
        QWidget.__init__(self, parent=parent)
        self.central_layout = QtWidgets.QVBoxLayout()
        self.list_view = QtWidgets.QListView()
        self.path_label = QtWidgets.QLabel("Path: ")
        self.path_line_edit = QtWidgets.QLineEdit()
        self.open_button = QtWidgets.QPushButton("Open")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.central_layout.addWidget(self.list_view)
        self.file_model = QtWidgets.QFileSystemModel()
        self.file_model.setFilter(QDir.AllEntries)
        self.file_model.setRootPath("")
        self.file_data = list(list())
        self.test_data = None
        self.list_view.setModel(self.file_model)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addWidget(self.path_label)
        horizontal_layout.addWidget(self.path_line_edit)
        self.central_layout.addLayout(horizontal_layout)

        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.addSpacerItem(QtWidgets.QSpacerItem(150, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        horizontal_layout.addWidget(self.open_button)
        horizontal_layout.addWidget(self.cancel_button)
        self.central_layout.addLayout(horizontal_layout)

        self.list_view.doubleClicked.connect(self.double_click_slots)
        self.open_button.clicked.connect(self.ok_button_clicked)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

        self.setLayout(self.central_layout)
        self.initUi()

    def initUi(self):
        _translate = QtCore.QCoreApplication.translate

    def double_click_slots(self, index):
        file_info = self.file_model.fileInfo(index)
        if file_info.fileName() == "..":
            dir = file_info.dir()
            dir.cdUp()
            self.list_view.setRootIndex(self.file_model.index(dir.absolutePath()))
            self.path_line_edit.setText("")
        elif file_info.fileName() == ".":
            self.list_view.setRootIndex(self.file_model.index(""))
            self.path_line_edit.setText("")
        elif file_info.isDir():
            self.list_view.setRootIndex(index)
            self.path_line_edit.setText("")
        elif file_info.isFile():
            dir = file_info.dir()
            self.path_line_edit.setText(str(dir.absolutePath())+"/"+file_info.fileName())

    def ok_button_clicked(self):
        self.file_data = pd.read_csv(self.path_line_edit.text(), delimiter=';')
        print(self.file_data)
        self.close()

    def cancel_button_clicked(self):
        self.close()
