from enum import IntEnum

from PyQt5.QtGui import (
    QColor,
    QImage,
)

IMG_BOMB = QImage("/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/bomb.png")
IMG_FLAG = QImage("/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/flag.png")
IMG_START = QImage("/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/rocket.png")
IMG_CLOCK = QImage("/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/clock-select.png")

NUM_COLORS = {
    1: QColor("#f44336"),
    2: QColor("#9C27B0"),
    3: QColor("#3F51B5"),
    4: QColor("#03A9F4"),
    5: QColor("#00BCD4"),
    6: QColor("#4CAF50"),
    7: QColor("#E91E63"),
    8: QColor("#FF9800"),
}

LEVELS = [(8, 10), (16, 40), (24, 99)]


class Status(IntEnum):
    READY = 0
    PLAYING = 1
    FAILED = 2
    SUCCESS = 3


STATUS_ICONS = {
    Status.READY: "/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/plus.png",
    Status.PLAYING: "/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/smiley.png",
    Status.FAILED: "/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/cross.png",
    Status.SUCCESS: "/Users/mikhailstreltsov/Desktop/desktopGit/AlgoritmAndPython/TvorkZad/images/smiley-lol.png",
}