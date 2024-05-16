from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QWidget, QLineEdit

import sys


class Calclulator(QWidget):
    def __init__(self):
        super().__init__()
        self.formUI()

    def formUI(self):
        self.setGeometry(1200, 500, 320, 80)
        self.setWindowTitle("Задание 1")

        self.textExample = QLabel(self)
        self.textExample.setText("Выражение: ")
        self.textExample.move(10,10)

        self.textExampleResult = QLabel(self)
        self.textExampleResult.setText("Результат: ")
        self.textExampleResult.move(180,10)

        self.inputExample = QLineEdit(self)
        self.inputExample.move(10,30)

        self.inputExampleResult = QLineEdit(self)
        self.inputExampleResult.move(180,30)

        self.buttonResult = QPushButton("->", self)
        self.buttonResult.resize(32, 32)
        self.buttonResult.move(150, 29)
        self.buttonResult.clicked.connect(self.calculate)

    def calculate(self):
        digits = self.inputExample.text()
        code = compile(f"{digits}", "<string>", "eval")
        code = eval(code)
        self.inputExampleResult.setText(f"{code}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calclulator()
    calc.show()
    sys.exit(app.exec())



