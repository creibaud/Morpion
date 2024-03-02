import pygame
from src.constants import *

class Cell:
    def __init__(self, row: int, col: int, content: str) -> None:
        """
        Constructor for the Cell class

        Args:
            row (int): The row number of the cell
            col (int): The column number of the cell
            content (str): The content of the cell, either "X", "O" or " "
        
        Returns:
            None
        """

        self.x = col * CELL_SIZE + MARGIN_LEFT
        self.y = row * CELL_SIZE + MARGIN_TOP
        self.rect = pygame.Rect((self.x + CELL_SPACE_BETWEEN, self.y + CELL_SPACE_BETWEEN), (CELL_SIZE - 2 * CELL_SPACE_BETWEEN, CELL_SIZE - 2 * CELL_SPACE_BETWEEN))
        self.content = content
        self.color = CELL_BG

    def drawX(self, screen: pygame.Surface) -> None:
        """
        Draws an X on the cell

        Args:
            screen (pygame.Surface): The surface to draw the X on (the game window)
        
        Returns:
            None
        """

        x1 = self.x + CELL_SPACE_BETWEEN + 35
        y1 = self.y + CELL_SPACE_BETWEEN + 30
        x2 = self.x + CELL_SIZE - CELL_SPACE_BETWEEN - 35
        y2 = self.y + CELL_SIZE - CELL_SPACE_BETWEEN - 30
        pygame.draw.lines(screen, X_CELL, False, [(x1, y1), (x2, y2)], 15)
        pygame.draw.lines(screen, X_CELL, False, [(x1, y2), (x2, y1)], 15)

    def drawO(self, screen: pygame.Surface) -> None:
        """
        Draws an O on the cell

        Args:
            screen (pygame.Surface): The surface to draw the O on (the game window)
        
        Returns:
            None
        """

        pygame.draw.circle(screen, O_CELL, self.rect.center, (CELL_SIZE - 2 * CELL_SPACE_BETWEEN - 45) / 2, 15)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the cell on the screen

        Args:
            screen (pygame.Surface): The surface to draw the cell on (the game window)
        
        Returns:
            None
        """

        pygame.draw.rect(screen, self.color, self.rect, border_radius = 10)
        if self.content == "X":
            self.drawX(screen)
        elif self.content == "O":
            self.drawO(screen)