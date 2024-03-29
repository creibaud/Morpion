import pygame
from src.grid import Grid
from src.panel import Panel
from src.line import Line

class Offline:
    def __init__(self) -> None:
        """
        Constructor for the Offline class

        Args:
            None
        
        Returns:
            None
        """

        self.grid = Grid()
        self.panel = Panel()
        self.line = Line()

        self.player = "X"
        self.gameOver = False

    def handleMouseHover(self, pos: tuple[int, int]) -> None:
        """
        Handles the mouse hover event

        Args:
            pos (tuple[int, int]): The position of the mouse
        
        Returns:
            None
        """

        self.grid.handleMouseHover(pos, self.gameOver)
    
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
    
    def isGameOver(self) -> None:
        """
        Checks if the game is over

        Args:
            None
        
        Returns:
            None
        """

        winner = self.grid.checkWinner(self.player)
        if winner:
            self.panel.winner = self.player
            self.gameOver = True
        else:
            tie = self.grid.isTie()
            if tie:
                self.panel.tie = True
                self.gameOver = True

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the game

        Args:
            screen (pygame.Surface): The surface to draw the game on (the game window)
        
        Returns:
            None
        """
        
        self.grid.draw(screen)
        self.panel.draw(screen)

        if self.gameOver:
            self.line.draw(screen, self.grid.grid)