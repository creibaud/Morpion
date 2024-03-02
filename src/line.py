import pygame
from src.constants import *

class Line:
    def __init__(self) -> None:
        """
        Constructor for the Line class

        Args:
            None
        
        Returns:
            None
        """

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.color = PANEL_BG_END

    def checkHowVictory(self, grid: list[list[str]]) -> bool:
        """
        Checks how the game was won

        Args:
            grid (list[list[str]]): The grid of the game
        
        Returns:
            bool: True if the game was won, False otherwise
        """

        for i in range(0, ROWS):
            if grid[i][0] == grid[i][1] == grid[i][2] != "":
                self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
                self.y1 = CELL_SIZE * i + MARGIN_TOP + CELL_SIZE / 2
                self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
                self.y2 = self.y1
                return True
                
        for i in range(0, COLS):
            if grid[0][i] == grid[1][i] == grid[2][i] != "":
                self.x1 = CELL_SIZE * i + MARGIN_LEFT + CELL_SIZE / 2
                self.y1 = MARGIN_TOP + CELL_SPACE_BETWEEN + 20
                self.x2 = self.x1
                self.y2 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 20
                return True
                
        if grid[0][0] == grid[1][1] == grid[2][2] != "":
            self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
            self.y1 = MARGIN_TOP + CELL_SPACE_BETWEEN + 15
            self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
            self.y2 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 15
            return True
        
        if grid[0][2] == grid[1][1] == grid[2][0] != "":
            self.x1 = MARGIN_LEFT + CELL_SPACE_BETWEEN + 20
            self.y1 = CELL_SIZE * 3 + MARGIN_TOP - CELL_SPACE_BETWEEN - 15
            self.x2 = CELL_SIZE * 3 + MARGIN_LEFT - CELL_SPACE_BETWEEN - 20
            self.y2 = MARGIN_TOP + CELL_SPACE_BETWEEN + 15
            return True

        return False
    
    def draw(self, screen: pygame.Surface, grid: list[list[str]]) -> None:
        """
        Draws the line of the victory

        Args:
            screen (pygame.Surface): The screen to draw on
            grid (list[list[str]]): The grid of the game
        
        Returns:
            None
        """

        if self.checkHowVictory(grid):
            pygame.draw.lines(screen, self.color, True, [(self.x1, self.y1), (self.x2, self.y2)], 10)