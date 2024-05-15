import sys
from random import randint
from PyQt5.QtWidgets import (QApplication, QMainWindow, QInputDialog,
                               QWidget, QLabel,
                               QVBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap, QColor


class Flag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.formUI()


    def formUI(self):
        self.setGeometry(1200, 800, 200, 200)
        self.setWindowTitle("Генерация флага")

        self.main = QWidget()
        self.layout = QVBoxLayout()
        self.main.setLayout(self.layout)


        self.openModal = QPushButton('Ввести количество цветов флага')
        self.openModal.clicked.connect(self.modalWin)
        self.layout.addWidget(self.openModal)
       
        self.flagBlock = QVBoxLayout()
        self.flagBlock.setSpacing(0)
        self.flagBlock.addStretch()

        self.layout.addLayout(self.flagBlock)

        self.setCentralWidget(self.main)


    def modalWin(self):
        colorCount, ok = QInputDialog.getInt(self,
                                              'Введите число цветов флага',
                                              'Сколько цветов?', 3, 1, 10, 1)

        if ok:
            self.draw_flag(colorCount)

    def draw_flag(self, color_count):
        for i in range(color_count):
            flagPart = QLabel()
            partColor = QPixmap(200, 20)
            randomColor = QColor(randint(0, 255),
                                  randint(0, 255),
                                  randint(0, 255))
            partColor.fill(randomColor)
            flagPart.setPixmap(partColor)
            self.flagBlock.addWidget(flagPart)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menuBlins = Flag()
    menuBlins.show()
    sys.exit(app.exec())