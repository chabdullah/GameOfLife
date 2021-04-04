# GameOfLife
# Overview
![GitHub last commit](https://img.shields.io/github/last-commit/chabdullah/gameOfLife)
- **Academic year:** 2020-2021
- **Project title:** Game of Life
- **Student:** [Abdullah Chaudhry](https://github.com/chabdullah)
- **CFUs:** 9

## About Game of Life
The game of life is a cellular automaton imagined by John H. Conway in the 1970s and is probably, the best known of all cellular automata. Despite very simple rules, the game of life is Turing-complete and deterministic.
The game of life is a game in the mathematical sense rather than a playable game. It is “zero player game”.
* [Original article](http://ddi.cs.uni-potsdam.de/HyFISCH/Produzieren/lis_projekt/proj_gamelife/ConwayScientificAmerican.htm)
* [Online community](https://www.conwaylife.com/)

<img src="https://github.com/chabdullah/GameOfLife/blob/master/img/gameOfLifeDemo.gif">

## Rules
The game takes place on a two-dimensional finite or infinite grid whose cells can take two distinct states: “alive” or “dead”.
At each stage, the evolution of a cell is entirely determined by its current state and the state of its eight neighbours as follows:
1) A dead cell with exactly three living neighbours becomes alive.
2) A living cell with two or three living neighbours remains alive.
3) In all other cases, the cell becomes (or remains) dead.

## Implementation
The game was implemnted using Python and PyQt5 for the GUI.
The main feature have been written in the `Grid` class (`grid.py`) which represents the model of the MOV design pattern, in fact it provides methods to the controller (`GoL` class in `main.py`) in order to change the state of the game.   

### Functionality
The user can play, pause and reset the game using the buttons at the top of the window. The speed of the game can be changed at any time using a slider.

### Cell history
The animation of the Game of Life simulation keep track of how long each cell has been alive. Each cell remembers for how long it has been
occupied and changes accordingly the color from light blue (newborn) to bright red (ancient).

## Requirements
**PyQt5**
```console
$ pip install PyQt5
```
## Running the game
The game can be launched from the `main.py` script:
```
$ python3 main.py
```

# Acknowledgments
Human Computer Interaction project - Computer Engineering Master Degree @[University of Florence](https://www.unifi.it/changelang-eng.html)
