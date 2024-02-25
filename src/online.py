import pickle
from src.grid import Grid
from src.panel import Panel
from src.line import Line
from src.client import Client

class Online:
    def __init__(self, host, port):
        self.grid = Grid()
        self.panel = Panel()
        self.line = Line()

        self.client = Client(host, port)
        self.client.start()

        self.player = self.client.name
        self.actualPlayer = "X"
        self.isClientTurn = False if self.player == "O" else True
        self.gameOver = False
        self.enemyMove = []

    def handleMouseHover(self, pos):
        self.grid.handleMouseHover(pos, self.gameOver)
    
    def handleMouseClick(self, pos):
        if self.grid.handleMouseClick(pos, self.player, self.gameOver):
            self.actualPlayer = "X" if self.actualPlayer == "O" else "X"
            self.panel.update(self.actualPlayer)
            self.client.send(pos)
            self.isClientTurn = False
    
    def isGameOver(self):
        winner = self.grid.checkWinner(self.actualPlayer)
        if winner:
            self.panel.winner = self.actualPlayer
            self.gameOver = True
        else:
            tie = self.grid.isTie()
            if tie:
                self.panel.tie = True
                self.gameOver = True

    def update(self):
        if not self.isClientTurn and len(self.enemyMove) < len(self.client.enemyMove):
            pos = self.grid.convertPosToCell(self.client.enemyMove[-1])
            self.enemyMove.append(pos)
            self.grid.makeMove(pos, "O" if self.player == "X" else "X")
            self.isClientTurn = True

    def draw(self, screen):
        self.isGameOver()
        self.update()
        self.grid.draw(screen)
        self.panel.draw(screen)

        if self.gameOver:
            self.line.draw(screen, self.grid.grid)