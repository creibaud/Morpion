import pygame
from src.constants import *
from src.cell import Cell

class Grid:
    def __init__(self) -> None:
        """
        Constructor for the Grid class

        Args:
            None
        
        Returns:
            None
        """

        self.grid = self.initGrid()
        self.cells = self.initCells()

    def initGrid(self) -> list[str]:
        """
        Initializes the grid with empty strings

        Args:
            None

        Returns:
            list[str]: The initialized grid as a list of strings
        """

        grid = []
        for row in range(ROWS):
            grid.append([])
            for col in range(COLS):
                grid[row].append("")
        return grid
    
    def initCells(self) -> list[Cell]:
        """
        Initializes the cells of the grid

        Args:
            None

        Returns:
            list[Cell]: The initialized cells of the grid
        """

        cells = []
        for row in range(ROWS):
            cells.append([])
            for col in range(COLS):
                cells[row].append(Cell(row, col, self.grid[row][col]))
        return cells
    
    def getEmptyCells(self) -> list[tuple[int, int]]:
        """
        Returns a list of empty cells (position) in the grid

        Args:
            None
        
        Returns:
            list[tuple[int, int]]: A list of empty cells in the grid
        """

        cells = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == "":
                    cells.append((row, col))
        return cells
    
    def handleMouseHover(self, pos: tuple[int, int], gameOver: bool) -> None:
        """
        Handles the mouse hover event

        Args:
            pos (tuple[int, int]): The position of the mouse
            gameOver (bool): The game over status
        
        Returns:
            None
        """

        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos) and self.grid[row][col] == "" and not gameOver:
                    self.cells[row][col].color = CELL_BG_HOVER
                else:
                    self.cells[row][col].color = CELL_BG
    
    def handleMouseClick(self, pos: tuple[int, int], player: str, gameOver: bool) -> bool:
        """
        Handles the mouse click event

        Args:
            pos (tuple[int, int]): The position of the mouse
            player (str): The player making the move
            gameOver (bool): The game over status
        
        Returns:
            bool: True if the move was made, False otherwise
        """

        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos) and self.grid[row][col] == "" and not gameOver:
                    self.grid[row][col] = player
                    self.cells[row][col].content = player
                    return True
        return False
    
    def convertPosToCell(self, pos: tuple[int, int]) -> tuple[int, int] | None:
        """
        Converts the position of the mouse to the cell position

        Args:
            pos (tuple[int, int]): The position of the mouse
        
        Returns:
            tuple[int, int] | None: The cell position if the mouse is on a cell, None otherwise
        """

        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos):
                    return (row, col)
        return None

    def makeMove(self, move: tuple[int, int], player: str) -> None:
        """
        Makes a move on the grid

        Args:
            move (tuple[int, int]): The position of the move
            player (str): The player making the move
        
        Returns:
            None
        """

        self.grid[move[0]][move[1]] = player
        self.cells[move[0]][move[1]].content = player

    def undoMove(self, move: tuple[int, int]) -> None:
        """
        Undoes a move on the grid

        Args:
            move (tuple[int, int]): The position of the move
        
        Returns:
            None
        """

        self.grid[move[0]][move[1]] = ""
        self.cells[move[0]][move[1]].content = ""
    
    def checkWinner(self, player: str) -> bool:
        """
        Checks if the player has won the game

        Args:
            player (str): The player to check for
        
        Returns:
            bool: True if the player has won, False otherwise
        """

        for row in range(ROWS):
            if [self.grid[row][col] for col in range(COLS)] == [player] * COLS:
                return True
            
        for col in range(COLS):
            if [self.grid[row][col] for row in range(ROWS)] == [player] * ROWS:
                return True
            
        if [self.grid[i][i] for i in range(ROWS)] == [player] * ROWS:
            return True
        
        if [self.grid[i][ROWS - 1 - i] for i in range(ROWS)] == [player] * ROWS:
            return True
        
        return False

    def isTie(self) -> bool:
        """
        Checks if the game is a tie (is full or not)

        Args:
            None
        
        Returns:
            bool: True if the game is a tie, False otherwise
        """

        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == "":
                    return False
        return True
    
    def update(self) -> None:
        """
        Updates the cells of the grid

        Args:
            None
        
        Returns:
            None
        """

        for row in range(ROWS):
            for col in range(COLS):
                self.cells[row][col].content = self.grid[row][col]
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the grid on the screen

        Args:
            screen (pygame.Surface): The surface to draw the grid on (the game window)
        
        Returns:
            None
        """

        for row in range(ROWS):
            for col in range(COLS):
                self.cells[row][col].draw(screen)