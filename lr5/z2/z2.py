from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QWidget, QLineEdit, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.formUI()

    def formUI(self):
        self.setGeometry(1200, 500, 850, 800)
        self.setWindowTitle("Масленица")

        self.checkboxMed = QCheckBox("Мед", self)
        self.checkboxMed.move(10,10)
        self.checkboxMed.stateChanged.connect(self.show_med)

        self.checkboxSgush = QCheckBox("Сгущенка", self)
        self.checkboxSgush.move(60,10)
        self.checkboxSgush.stateChanged.connect(self.show_sgush)

        self.checkboxIkra = QCheckBox("Икра", self)
        self.checkboxIkra.move(140,10)
        self.checkboxIkra.stateChanged.connect(self.show_ikra)

        self.labelImgMain = QLabel(self)
        self.labelImgMain.move(50,60)
        self.mainImg = QPixmap(r"C:\Users\Mikhail\Desktop\GitHUb\AlgoritmAndPython\lr5\z2/blin.png")
        self.labelImgMain.setPixmap(self.mainImg)

        self.labelImgIkra = QLabel(self)
        self.labelImgIkra.move(220,500)
        self.labelImgIkra.setPixmap(QPixmap(r"C:\Users\Mikhail\Desktop\GitHUb\AlgoritmAndPython\lr5\z2/ikra.png"))
        self.labelImgIkra.hide()

        self.labelImgMed = QLabel(self)
        self.labelImgMed.move(0,500)
        self.labelImgMed.setPixmap(QPixmap(r"C:\Users\Mikhail\Desktop\GitHUb\AlgoritmAndPython\lr5\z2/med.png"))
        self.labelImgMed.hide()

        self.labelImgSgush = QLabel(self)
        self.labelImgSgush.move(520,500)
        self.labelImgSgush.setPixmap(QPixmap(r"C:\Users\Mikhail\Desktop\GitHUb\AlgoritmAndPython\lr5\z2/sgush.png"))
        self.labelImgSgush.hide()

    def show_ikra(self, state):
        if state == Qt.Checked:
            self.labelImgIkra.show()
        else:
            self.labelImgIkra.hide()
    
    def show_med(self, state):
        if state == Qt.Checked:
            self.labelImgMed.show()
        else:
            self.labelImgMed.hide()

    def show_sgush(self, state):
        if state == Qt.Checked:
            self.labelImgSgush.show()
        else:
            self.labelImgSgush.hide()
  
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuBlins = Menu()
    menuBlins.show()
    sys.exit(app.exec())
