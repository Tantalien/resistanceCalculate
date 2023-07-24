import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import math


Form, _ = uic.loadUiType('work project.ui')

resistance = 0

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('calc.png'))
        self.setWindowTitle('super-puper calculator')
        self.pushButton.clicked.connect(self.RWire_calc)
        self.pushButton.clicked.connect(self.UVoltage_calc)


    def RWire_calc(self):
        global resistance
        try:
            lenght = float(self.lineEdit.text()) #длина двухпроводного кабеля

            if self.radioButton.isChecked():  # расчет по площади
                square = float(self.lineEdit_2.text())
                resistance = 2 * (0.0175 * lenght) / square   # R = 2 * (p * l) / S

            else:  # расчет по диаметру
                cross = float(self.lineEdit_2.text())
                resistance = 2 * (0.0175 * lenght) / (0.785 * cross**2)  # R = 2 * (p * l) / (0.785 * D^2)

            self.label_5.setText(f'{resistance:.6f}')


        except Exception as err:
            self.label_5.setText(f'{err}')

    def UVoltage_calc(self):
        global resistance
        print(resistance)
        try:
            sensor_power = float(self.lineEdit_5.text())  #мощность потребления сенсора
            voltage_U0 = float(self.lineEdit_6.text())    #номинальное напряжение источника питания
            sensor_voltage = -0.5 * (-1 * voltage_U0 - math.sqrt((voltage_U0 ** 2) - (4 * sensor_power * resistance))) #напряжение питания сенсора с учетом падения напряжения на линии связи
            self.label_23.setText(f'{sensor_voltage:.6f}')


        except Exception as err:
            self.label_23.setText(f'{err}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()
