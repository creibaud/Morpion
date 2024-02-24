from src.grid import Grid
from src.panel import Panel
from src.line import Line

class Offline:
    def __init__(self):
        self.grid = Grid()
        self.panel = Panel()
        self.line = Line()

        self.player = "X"
        self.gameOver = False

    def handleMouseHover(self, pos):
        self.grid.handleMouseHover(pos, self.gameOver)
    
    def handleMouseClick(self, pos):
        if self.grid.handleMouseClick(pos, self.player, self.gameOver):
            self.isGameOver()
            self.player = "O" if self.player == "X" else "X"
            self.panel.update(self.player)
    
    def isGameOver(self):
        winner = self.grid.checkWinner(self.player)
        if winner:
            self.panel.winner = self.player
            self.gameOver = True
        else:
            tie = self.grid.isTie()
            if tie:
                self.panel.tie = True
                self.gameOver = True

    def draw(self, screen):
        self.grid.draw(screen)
        self.panel.draw(screen)

        if self.gameOver:
            self.line.draw(screen, self.grid.grid)