import pygame
from src.constants import *
from src.offline import Offline
from src.ia import IA
from src.online import Online

def menu():
    global game
    global screen
    
    font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
    fontTitle = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 60)
    title = fontTitle.render("Menu", True, O_CELL)

    offlineButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 200, 200, 100)
    offlineText = font.render("Offline", True, X_CELL)

    iaButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 350, 200, 100)
    iaText = font.render("IA", True, X_CELL)

    onlineButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 500, 200, 100)
    onlineText = font.render("Online", True, X_CELL)

    run = True
    while run:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if offlineButton.collidepoint(mousePos):
                        game = Offline()
                        run = False
                    elif iaButton.collidepoint(mousePos):
                        game = IA(4)
                        run = False
                    elif onlineButton.collidepoint(mousePos):
                        game = Online()
                        run = False
        
        screen.fill(BG_COLOR)

        screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 50))

        if offlineButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, offlineButton)
        else:
            pygame.draw.rect(screen, CELL_BG, offlineButton)

        screen.blit(offlineText, (SCREEN_WIDTH / 2 - offlineText.get_width() / 2, offlineButton.y + offlineText.get_height() / 2))

        if iaButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, iaButton)
        else:
            pygame.draw.rect(screen, CELL_BG, iaButton)
        
        screen.blit(iaText, (SCREEN_WIDTH / 2 - iaText.get_width() / 2, iaButton.y + iaText.get_height() / 2))

        if onlineButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, onlineButton)
        else:
            pygame.draw.rect(screen, CELL_BG, onlineButton)

        screen.blit(onlineText, (SCREEN_WIDTH / 2 - onlineText.get_width() / 2, onlineButton.y + onlineText.get_height() / 2))

        pygame.display.flip()
        clock.tick(FPS)

def menuDifficulty():
    global game
    global screen
    
    font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
    fontTitle = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 60)
    title = fontTitle.render("Difficulty", True, O_CELL)

    easyButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 200, 200, 100)
    easyText = font.render("Easy", True, X_CELL)

    mediumButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 350, 200, 100)
    mediumText = font.render("Medium", True, X_CELL)

    hardButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 500, 200, 100)
    hardText = font.render("Hard", True, X_CELL)

    run = True
    while run:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easyButton.collidepoint(mousePos):
                        game = IA(1)
                        run = False
                    elif mediumButton.collidepoint(mousePos):
                        game = IA(4)
                        run = False
                    elif hardButton.collidepoint(mousePos):
                        game = IA(9)
                        run = False
        
        screen.fill(BG_COLOR)

        screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 50))

        if easyButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, easyButton)
        else:
            pygame.draw.rect(screen, CELL_BG, easyButton)
        
        screen.blit(easyText, (SCREEN_WIDTH / 2 - easyText.get_width() / 2, easyButton.y + easyText.get_height() / 2))

        if mediumButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, mediumButton)
        else:
            pygame.draw.rect(screen, CELL_BG, mediumButton)
        
        screen.blit(mediumText, (SCREEN_WIDTH / 2 - mediumText.get_width() / 2, mediumButton.y + mediumText.get_height() / 2))

        if hardButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, hardButton)
        else:
            pygame.draw.rect(screen, CELL_BG, hardButton)
        
        screen.blit(hardText, (SCREEN_WIDTH / 2 - hardText.get_width() / 2, hardButton.y + hardText.get_height() / 2))

        pygame.display.flip()
        clock.tick(FPS)

def menuChoiceSymbol():
    global game
    global screen

    font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
    fontTitle = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 60)
    title = fontTitle.render("Choose symbol", True, O_CELL)

    xButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 200, 200, 100)
    xText = font.render("X", True, X_CELL)

    oButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 350, 200, 100)
    oText = font.render("O", True, X_CELL)

    run = True
    while run:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if xButton.collidepoint(mousePos):
                        game.setStartingPlayer("X")
                        run = False
                    elif oButton.collidepoint(mousePos):
                        game.setStartingPlayer("O")
                        run = False
        
        screen.fill(BG_COLOR)

        screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 50))

        if xButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, xButton)
        else:
            pygame.draw.rect(screen, CELL_BG, xButton)
        
        screen.blit(xText, (SCREEN_WIDTH / 2 - xText.get_width() / 2, xButton.y + xText.get_height() / 2))

        if oButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, oButton)
        else:
            pygame.draw.rect(screen, CELL_BG, oButton)
        
        screen.blit(oText, (SCREEN_WIDTH / 2 - oText.get_width() / 2, oButton.y + oText.get_height() / 2))

        pygame.display.flip()
        clock.tick(FPS)

def start():
    global game
    global screen

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

def restart():
    global game
    global screen
    global restartGame

    game = None

    menu()
    if type(game) == IA:
        menuDifficulty()
        menuChoiceSymbol()
    start()

    if type(game) == Online:
        game.stop()

    font = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 40)
    fontTitle = pygame.font.Font("assets/fonts/Roboto/Roboto-Medium.ttf", 60)
    title = fontTitle.render("Restart ?", True, O_CELL)

    yesButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 200, 200, 100)
    yesText = font.render("Yes", True, X_CELL)

    noButton = pygame.Rect(SCREEN_WIDTH / 2 - 100, 350, 200, 100)
    noText = font.render("No", True, X_CELL)

    run = True
    while run:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yesButton.collidepoint(mousePos):
                        restartGame = True
                        run = False
                    elif noButton.collidepoint(mousePos):
                        restartGame = False
                        run = False
        
        screen.fill(BG_COLOR)

        screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, 50))

        if yesButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, yesButton)
        else:
            pygame.draw.rect(screen, CELL_BG, yesButton)
        
        screen.blit(yesText, (SCREEN_WIDTH / 2 - yesText.get_width() / 2, yesButton.y + yesText.get_height() / 2))

        if noButton.collidepoint(mousePos):
            pygame.draw.rect(screen, CELL_BG_HOVER, noButton)
        else:
            pygame.draw.rect(screen, CELL_BG, noButton)
        
        screen.blit(noText, (SCREEN_WIDTH / 2 - noText.get_width() / 2, noButton.y + noText.get_height() / 2))

        pygame.display.flip()
        clock.tick(FPS)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Morpion")

icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
game = None
restartGame = True

while restartGame:
    restart()

pygame.quit()