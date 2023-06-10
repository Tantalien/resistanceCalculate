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
        self.pushButton_2.clicked.connect(self.RDevice)
        self.pushButton.clicked.connect(self.RWire_calc)


    def RWire_calc(self):
        try:
            lenght = float(self.lineEdit.text())

            if self.radioButton.isChecked():  # расчет по площади
                square = float(self.lineEdit_2.text())
                resistance = ((1.6e-8) * lenght) / (square / 1e6)   # R = (p * l) / S

            else:  # расчет по диаметру
                cross = float(self.lineEdit_2.text())
                resistance = ((1.6e-8) * lenght) / (0.785 * cross**2 / 1e6)  # R = (p * l) / S

            self.label_5.setText(f'{resistance:.6f}')

        except Exception as err:
            self.label_5.setText(f'{err}')



    def RDevice(self):
        global a
        global b
        global c
        a = float(self.lineEdit_3.text())
        b = float(self.lineEdit_4.text())
        c = a / b
        d = b / c
        d = ("%.6f" % d)
        i = f'{d}'
        self.label_13.setText(i)







'''    def onMyButtonClick_2(self):
        global otvet
        if otvet == "0":
            self.label_2.setText("Ответ не выбран")
        elif otvet == "rb1":
            self.label_2.setText("Верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: green}')
        elif otvet == "rb2":
            self.label_2.setText("Не верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: red}')
        elif otvet == "rb3":
            self.label_2.setText("Не верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: red}')

    def choise(self, button):
        global otvet
        otvet = button.objectName()'''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()
