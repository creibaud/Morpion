import pygame
from src.constants import *
from src.offline import Offline
from src.ia import IA
from src.online import Online

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Morpion")

icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
game = None

while True:
    try:
        mode = int(input("Choose a mode (1: Offline, 2: IA, 3:Online): "))
        if mode in [1, 2, 3]:
            match mode:
                case 1:
                    game = Offline()
                    break
                case 2:
                    while True:
                        try:
                            difficulty = int(input("Choose a difficulty (1: Easy, 2: Medium, 3: Hard): "))
                            if difficulty in [1, 2, 3]:
                                match difficulty:
                                    case 1:
                                        game = IA(1)
                                        break
                                    case 2:
                                        game = IA(4)
                                        break
                                    case 3:
                                        game = IA(9)
                                        break
                                break
                            else:
                                raise ValueError("Invalid difficulty")
                        except ValueError as e:
                            print(e)
                    break
                case 3:
                    game = Online()
                    break
        else:
            raise ValueError("Invalid mode")
    except ValueError as e:
        print(e)

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
if type(game) == Online:
    game.stop()