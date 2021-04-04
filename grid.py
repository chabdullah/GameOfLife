from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget


class Cell(QWidget):
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        self.colorsSpeed = 20
        self.colorHistory = 0
        self.stateColor = 'white'
        self.alive = False
        self.next_state = False

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setBrush(QColor(self.stateColor))
        p.drawRect(0, 0, 100, 100)
        p.end()

    def mousePressEvent(self, event):
        if self.alive:
            self.stateColor = 'white'
            self.die()
        else:
            self.stateColor = QColor(0, 255, 255)
            self.live()
        self.update()

    def die(self):
        self.alive = False

    def live(self):
        self.alive = True

    def updateState(self):
        if self.next_state:
            if self.colorHistory + self.colorsSpeed < 255:
                self.colorHistory += self.colorsSpeed
            self.stateColor = QColor(self.colorHistory, 255 - self.colorHistory, 255 - self.colorHistory)
            self.live()
        else:
            self.colorHistory = 0
            self.stateColor = 'white'
            self.die()
        self.update()


class Grid(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.setLayout(self.grid)

        self.x_length = 30
        self.y_length = 30
        for x in range(self.x_length):
            for y in range(self.y_length):
                cell = Cell()
                self.grid.addWidget(cell, x, y)
        self.timer = QBasicTimer()
        self.on = False
        self.clearGame()

    def timerEvent(self, event):
        for i in range(self.grid.count()):
            x, y = self.grid.getItemPosition(i)[0], self.grid.getItemPosition(i)[1]
            cell = self.grid.itemAt(i).widget()
            self.futureState(cell, x, y)

        for i in range(self.grid.count()):
            self.grid.itemAt(i).widget().updateState()

    def startGame(self):
        self.timer.start(self.speed, self)
        self.on = True

    def pauseGame(self):
        self.timer.stop()
        self.on = False

    def clearGame(self):
        self.pauseGame()
        for x in range(self.x_length):
            for y in range(self.y_length):
                self.grid.itemAtPosition(x, y).widget().alive = False
                self.grid.itemAtPosition(x, y).widget().next_state = False
                self.grid.itemAtPosition(x, y).widget().stateColor = 'white'
        self.update()

    def futureState(self, cell, x, y):
        alive_neighbors = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    if not (i == j == 0) and self.grid.itemAtPosition(x + i, y + j).widget().alive:
                        alive_neighbors += 1
                except:
                    pass
        if cell.alive and (2 <= alive_neighbors <= 3):
            cell.next_state = cell.alive
        elif not cell.alive and alive_neighbors == 3:
            cell.next_state = True
        elif cell.alive and (alive_neighbors < 2 or alive_neighbors > 3):
            cell.next_state = False