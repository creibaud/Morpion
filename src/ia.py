from src.grid import Grid
from src.panel import Panel
from src.line import Line

class IA:
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
            
            _, bestMove = self.minMax(self.player, True)
            if bestMove is not None:
                self.grid.makeMove(bestMove, self.player)

            self.isGameOver()
            self.player = "O" if self.player == "X" else "X"
            self.panel.update(self.player)

    def minMax(self, symbol, maximizingPlayer):
        if self.grid.isTie() or self.grid.checkWinner("X") or self.grid.checkWinner("O"):
            if self.grid.checkWinner("X"):
                return -1 if symbol == "O" else 1, None
            elif self.grid.checkWinner("O"):
                return -1 if symbol == "X" else 1, None
            else:
                return 0, None

        if maximizingPlayer:
            maxEval = float("-inf")
            bestMove = None
            for move in self.grid.getEmptyCells():
                self.grid.makeMove(move, symbol)
                eval, _ = self.minMax(symbol, False)
                self.grid.undoMove(move)
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
            return maxEval, bestMove
        else:
            minEval = float("inf")
            bestMove = None
            opponent = "X" if symbol == "O" else "O"
            for move in self.grid.getEmptyCells():
                self.grid.makeMove(move, opponent)
                eval, _ = self.minMax(symbol, True)
                self.grid.undoMove(move)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
            return minEval, bestMove

    
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