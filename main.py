import random
import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import math

Form, _ = uic.loadUiType('work project.ui')

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.RDevice_calc)
        self.pushButton.clicked.connect(self.RWire_calc)


    def RWire_calc(self):
        try:
            lenght = float(self.lineEdit.text())

            if self.radioButton.isChecked():  # расчет по площади
                square = float(self.lineEdit_2.text())
                resistance = ((1.6e-8) * lenght) / (square / 1e6)   # R = (p * l) / S

            else:  # расчет по диаметру
                cross = float(self.lineEdit_2.text())
                resistance = ((1.6e-8) * lenght) / (0.785 * cross**2 / 1e6)  # R = (p * l) / (0.785 * D^2)

            self.label_5.setText(f'{resistance:.6f}')

        except Exception as err:
            self.label_5.setText(f'{err}')


    def RDevice_calc(self):
        try:
            power = float(self.lineEdit_3.text())
            voltage = float(self.lineEdit_4.text())
            amperage = power / voltage                     # I = P / U
            resistance = voltage / amperage                # R = U / I
            self.label_13.setText(f'{resistance:.6f}')

        except Exception as err:
            self.label_13.setText(f'{err}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()
