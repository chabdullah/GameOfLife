from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget


class Cell(QWidget):
    def __init__(self):
        super().__init__()
        self.colorsSpeed = 20   # The speed at which a cell change its color (cell history)
        self.colorHistory = 0   # Initial value with which it will be calculated cell's history
        self.stateColor = 'white'
        self.alive = False
        self.next_state = False  # Next state of a cell is calculated in futureState() method of Grid class

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setBrush(QColor(self.stateColor))
        p.drawRect(0, 0, 100, 100)
        p.end()

    # When the user click on a cell it changes it state from dead (white) to alive (light blue) or vice versa
    def mousePressEvent(self, event):
        if self.alive:
            self.stateColor = 'white'
            self.die()
        else:
            self.stateColor = QColor(0, 255, 255)   # The initial color is a light blue
            self.live()
        self.update()

    def die(self):
        self.alive = False

    def live(self):
        self.alive = True

    def updateState(self):
        if self.next_state:
            # The color (cell's history) changes from light blue (0,255,255) to red (255,0,0)
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
    def __init__(self, x, y):
        super().__init__()
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.setLayout(self.grid)

        self.x_length = x
        self.y_length = y
        # Initialize all the cells in the grid
        for x in range(self.x_length):
            for y in range(self.y_length):
                cell = Cell()
                self.grid.addWidget(cell, x, y)
        # Initialize the QBasicTimer which will be used to manage the update (refresh rate) of the view
        self.timer = QBasicTimer()
        self.on = False
        self.clearGame()

    def timerEvent(self, event):
        # Calculate the future state of every cell in the grid (without updating the view)
        for i in range(self.grid.count()):
            x, y = self.grid.getItemPosition(i)[0], self.grid.getItemPosition(i)[1]
            cell = self.grid.itemAt(i).widget()
            self.futureState(cell, x, y)
        # Update the view for all cells simultaneously
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
        # Initialize the state of all cells
        for x in range(self.x_length):
            for y in range(self.y_length):
                self.grid.itemAtPosition(x, y).widget().alive = False
                self.grid.itemAtPosition(x, y).widget().next_state = False
                self.grid.itemAtPosition(x, y).widget().stateColor = 'white'
        self.update()

    def futureState(self, cell, x, y):
        alive_neighbors = 0  # Calculate all alive neighbors of a particular cell
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == j == 0) and (x+i in range(0, self.x_length)) and (y+j in range(0, self.y_length))\
                        and self.grid.itemAtPosition(x + i, y + j).widget().alive:
                    alive_neighbors += 1
        # According to game's rules change cell's next state which will be updated later when
        # all cells will have calculated their respective next state
        if cell.alive and (2 <= alive_neighbors <= 3):
            cell.next_state = cell.alive
        elif not cell.alive and alive_neighbors == 3:
            cell.next_state = True
        elif cell.alive and (alive_neighbors < 2 or alive_neighbors > 3):
            cell.next_state = False
