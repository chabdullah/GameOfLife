import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSlider

from grid import Grid


class Gol(QMainWindow):

    def __init__(self):
        super().__init__()
        # Create main window
        self.setWindowTitle('Game of Life')
        self.grid = Grid()
        self.setCentralWidget(self.grid)
        x, y = (self.grid.x_length, self.grid.y_length)
        self.setFixedSize(x * 15, y * 15)
        # Create toolbar and add buttons
        self.toolbar = self.addToolBar('menu')
        self.playButton = QPushButton("Play", self)
        self.pauseButton = QPushButton("Pause", self)
        self.clearButton = QPushButton("Clear", self)
        self.playButton.clicked.connect(self.playGame)
        self.pauseButton.clicked.connect(self.pauseGame)
        self.clearButton.clicked.connect(self.clearGame)
        # View component (Slider) that controls the speed of the game
        self.initialSpeed = 500
        self.slider = QSlider(Qt.Horizontal)
        self.maximumSlider = 1000
        self.slider.setMinimum(10)
        self.slider.setMaximum(self.maximumSlider)
        self.slider.setValue(self.initialSpeed)
        self.grid.speed = self.initialSpeed
        self.slider.valueChanged.connect(self.sliderValueChange)

        self.toolbar.addWidget(self.playButton)
        self.toolbar.addWidget(self.pauseButton)
        self.toolbar.addWidget(self.clearButton)
        self.toolbar.addWidget(self.slider)

        self.show()

    # The controller will interact with the Model (Grid class) with these methods
    def playGame(self):
        self.grid.startGame()

    def pauseGame(self):
        self.grid.pauseGame()

    def clearGame(self):
        self.grid.clearGame()

    def sliderValueChange(self):
        self.grid.speed = (self.maximumSlider + 10) - self.slider.value()
        if self.grid.on:
            self.playGame()


def main():
    gol = QApplication(sys.argv)
    w = Gol()
    sys.exit(gol.exec_())


if __name__ == '__main__':
    main()