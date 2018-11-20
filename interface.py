from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, \
    QHBoxLayout, QVBoxLayout, QComboBox, QAction, QPushButton, QPlainTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.width = 150
        self.height = 400

        self.menu = self.menuBar()
        self.run_act = QAction('Iniciar Maquina')

        self.run_act.triggered.connect(self.iniciar)
        self.menu.addAction(self.run_act)

        operation_layout = QHBoxLayout()
        self.operation_select = QComboBox()
        self.first_operand = QPlainTextEdit()
        self.first_operand.setFixedWidth(10)
        self.second_operand = QPlainTextEdit()
        operation_layout.addWidget(self.operation_select)
        operation_layout.addWidget(self.first_operand)
        operation_layout.addWidget(self.second_operand)

        self.processing_tape = QTextEdit()

        layout = QVBoxLayout()
        layout.addLayout(operation_layout )
        layout.addWidget(self.processing_tape)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.setWindowTitle("Máquina de Turing")
        self.show()

    def iniciar(self):
        pass