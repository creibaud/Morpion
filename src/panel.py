import pygame
from src.constants import *

class Panel:
    def __init__(self) -> None:
        """
        Constructor for the Panel class

        Args:
            None
        
        Returns:
            None
        """

        self.font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
        self.rect = pygame.Rect((MARGIN_LEFT + 5, 50), (3 * CELL_SIZE - 10, 125))
        self.player = "X"
        self.playerX = "X's Turn"
        self.playerO = "O's Turn"
        self.winner = None
        self.tie = False

    def drawContent(self, screen: pygame.Surface) -> None:
        """
        Draws the content of the panel

        Args:
            screen (pygame.Surface): The screen to draw on
        
        Returns:
            None
        """

        xColor = X_CELL if self.player == "O" else CELL_BG
        oColor = O_CELL if self.player == "X" else CELL_BG
        screen.blit(self.font.render(self.playerX, True, xColor), (self.rect.x + 40, self.rect.y + 40))
        screen.blit(self.font.render(self.playerO, True, oColor), (self.rect.x + 250, self.rect.y + 40))

    def drawBackRect(self, screen: pygame.Surface) -> None:
        """
        Draws the background rectangle of the panel

        Args:
            screen (pygame.Surface): The screen to draw on
        
        Returns:
            None
        """

        color = X_CELL if self.player == "X" else O_CELL
        position = (MARGIN_LEFT + 15, self.rect.y + 15) if self.player == "X" else (MARGIN_LEFT + 235, self.rect.y + 15)
        rect = pygame.Rect(position, (200, 95))
        pygame.draw.rect(screen, color, rect, border_radius = 10)

    def update(self, player: str) -> None:
        """
        Updates the panel

        Args:
            player (str): The player

        Returns:
            None
        """

        self.player = player

    def drawWinner(self, screen: pygame.Surface) -> None:
        """
        Draws the winner

        Args:
            screen (pygame.Surface): The screen to draw on

        Returns:
            None
        """

        screen.blit(self.font.render(f"Player {self.winner} won !", True, CELL_BG), (self.rect.x + 100, self.rect.y + 40))

    def drawTie(self, screen: pygame.Surface) -> None:
        """
        Draws the tie

        Args:
            screen (pygame.Surface): The screen to draw on

        Returns:
            None
        """

        screen.blit(self.font.render("Tie !", True, CELL_BG), (self.rect.x + 185, self.rect.y + 40))

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the panel

        Args:
            screen (pygame.Surface): The screen to draw on

        Returns:
            None
        """

        if self.winner is not None or self.tie is True:
            pygame.draw.rect(screen, PANEL_BG_END, self.rect, border_radius = 10)
            self.drawWinner(screen) if self.winner is not None else self.drawTie(screen)
        else:
            pygame.draw.rect(screen, CELL_BG, self.rect, border_radius = 10)
            self.drawBackRect(screen)
            self.drawContent(screen)