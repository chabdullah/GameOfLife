import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSlider, QLabel, QComboBox, QToolBar

from grid import Grid


def setColor(widget, color):
    widget.setStyleSheet('QWidget {color: ' + color + '; padding: 10 ;}')


class Gol(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create main window
        self.setWindowTitle('Game of Life')
        self.size = 30
        self.grid = Grid(self.size, self.size)
        self.setCentralWidget(self.grid)
        self.setFixedSize(self.size * 15, self.size * 15)
        # Create toolbar and add buttons
        self.speedLabel = QLabel()
        self.speedLabel.setText("Speed")
        self.toolbar = self.addToolBar('menu')
        self.playButton = QPushButton("Play", self)
        self.pauseButton = QPushButton("Pause", self)
        self.clearButton = QPushButton("Clear", self)
        self.playButton.clicked.connect(self.playGame)
        self.pauseButton.clicked.connect(self.pauseGame)
        self.pauseButton.setDisabled(True)
        self.clearButton.clicked.connect(self.clearGame)
        # View component (Slider) that controls the speed of the game
        self.initialSpeed = 500
        self.sliderSpeed = QSlider(Qt.Horizontal)
        self.maximumSpeedSlider = 1000
        self.sliderSpeed.setMinimum(10)
        self.sliderSpeed.setMaximum(self.maximumSpeedSlider)
        self.sliderSpeed.setValue(self.initialSpeed)
        self.grid.speed = self.initialSpeed
        self.sliderSpeed.valueChanged.connect(self.sliderSpeedValueChange)
        # Add widgets to the toolbar
        self.toolbar.addWidget(self.playButton)
        self.toolbar.addWidget(self.pauseButton)
        self.toolbar.addWidget(self.clearButton)
        self.toolbar.addWidget(self.speedLabel)
        self.toolbar.addWidget(self.sliderSpeed)

        setColor(self.playButton, 'green')
        setColor(self.pauseButton, 'grey')
        setColor(self.clearButton, 'red')
        self.show()

    # The controller will interact with the Model (Grid class) with these methods
    def playGame(self):
        self.grid.startGame()
        setColor(self.playButton, 'grey')
        setColor(self.pauseButton, 'blue')
        self.playButton.setText('Simulating...')
        self.pauseButton.setDisabled(False)

    def pauseGame(self):
        self.grid.pauseGame()
        setColor(self.playButton, 'green')
        setColor(self.pauseButton, 'grey')
        self.playButton.setText('Resume')

    def clearGame(self):
        self.grid.clearGame()
        setColor(self.playButton, 'green')
        setColor(self.pauseButton, 'grey')
        self.playButton.setText('Play')
        self.pauseButton.setDisabled(True)

    def sliderSpeedValueChange(self):
        self.grid.speed = (self.maximumSpeedSlider + 10) - self.sliderSpeed.value()
        if self.grid.on:
            self.playGame()


def main():
    gol = QApplication(sys.argv)
    w = Gol()
    sys.exit(gol.exec_())


if __name__ == '__main__':
    main()