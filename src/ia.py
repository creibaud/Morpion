from src.offline import Offline
import random

class IA(Offline):
    def __init__(self, difficulty: int) -> None:
        """
        Constructor for the IA class

        Args:
            difficulty (int): The difficulty level of the IA
        
        Returns:
            None
        """

        super().__init__()
        self.difficulty = difficulty

    def setStartingPlayer(self, player: str) -> None:
        """
        Sets the starting player for the game

        Args:
            player (str): The starting player
        
        Returns:
            None
        """

        if player == "O":
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            self.grid.makeMove((row, col), "X")
            self.player = "O"
        else:
            self.player = "X"
    
    def handleMouseClick(self, pos: tuple[int, int]) -> None:
        """
        Handles the mouse click event

        Args:
            pos (tuple[int, int]): The position of the mouse

        Returns:
            None
        """

        if self.grid.handleMouseClick(pos, self.player, self.gameOver):
            self.isGameOver()
            self.player = "O" if self.player == "X" else "X"
            self.panel.update(self.player)
            
            _, bestMove = self.minMax(self.player, True, self.difficulty)
            if bestMove is not None:
                self.grid.makeMove(bestMove, self.player)

            self.isGameOver()
            self.player = "O" if self.player == "X" else "X"
            self.panel.update(self.player)

    def minMax(self, symbol: str, maximizingPlayer: bool, depth: int) -> tuple[int, int] | tuple[int, None]:
        """
        Minimax algorithm for the IA

        Args:
            symbol (str): The symbol of the player
            maximizingPlayer (bool): The maximizing player
            depth (int): The depth of the search
        
        Returns:
            tuple[int, int] | tuple[int, None]: The evaluation and the best move
        """

        if self.grid.isTie() or self.grid.checkWinner("X") or self.grid.checkWinner("O") or depth == 0:
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
                eval, _ = self.minMax(symbol, False, depth - 1)
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
                eval, _ = self.minMax(symbol, True, depth - 1)
                self.grid.undoMove(move)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
            return minEval, bestMove