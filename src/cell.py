import pygame
from src.constants import *

class Cell:
    def __init__(self, row, col, content):
        self.x = col * CELL_SIZE + MARGIN_LEFT
        self.y = row * CELL_SIZE + MARGIN_TOP
        self.rect = pygame.Rect((self.x + CELL_SPACE_BETWEEN, self.y + CELL_SPACE_BETWEEN), (CELL_SIZE - 2 * CELL_SPACE_BETWEEN, CELL_SIZE - 2 * CELL_SPACE_BETWEEN))
        self.content = content
        self.color = CELL_BG

    def drawX(self, screen):
        x1 = self.x + CELL_SPACE_BETWEEN + 35
        y1 = self.y + CELL_SPACE_BETWEEN + 30
        x2 = self.x + CELL_SIZE - CELL_SPACE_BETWEEN - 35
        y2 = self.y + CELL_SIZE - CELL_SPACE_BETWEEN - 30
        pygame.draw.lines(screen, X_CELL, False, [(x1, y1), (x2, y2)], 15)
        pygame.draw.lines(screen, X_CELL, False, [(x1, y2), (x2, y1)], 15)

    def drawO(self, screen):
        pygame.draw.circle(screen, O_CELL, self.rect.center, (CELL_SIZE - 2 * CELL_SPACE_BETWEEN - 45) / 2, 15)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 10)
        if self.content == "X":
            self.drawX(screen)
        elif self.content == "O":
            self.drawO(screen)