import pygame
from src.constants import *
from src.offline import Offline

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Morpion")

icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
game = Offline()

run = True
while run:
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.handleMouseClick(mousePos)

    screen.fill(BG_COLOR)
    
    game.handleMouseHover(mousePos)
    game.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()