from src.constants import *
from src.cell import Cell

class Grid:
    def __init__(self):
        self.grid = self.initGrid()
        self.cells = self.initCells()

    def initGrid(self):
        grid = []
        for row in range(ROWS):
            grid.append([])
            for col in range(COLS):
                grid[row].append("")
        return grid
    
    def initCells(self):
        cells = []
        for row in range(ROWS):
            cells.append([])
            for col in range(COLS):
                cells[row].append(Cell(row, col, self.grid[row][col]))
        return cells
    
    def getEmptyCells(self):
        cells = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == "":
                    cells.append((row, col))
        return cells
    
    def handleMouseHover(self, pos, gameOver):
        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos) and self.grid[row][col] == "" and not gameOver:
                    self.cells[row][col].color = CELL_BG_HOVER
                else:
                    self.cells[row][col].color = CELL_BG
    
    def handleMouseClick(self, pos, player, gameOver):
        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos) and self.grid[row][col] == "" and not gameOver:
                    self.grid[row][col] = player
                    self.cells[row][col].content = player
                    return True
        return False
    
    def convertPosToCell(self, pos):
        for row in range(ROWS):
            for col in range(COLS):
                if self.cells[row][col].rect.collidepoint(pos):
                    return (row, col)
        return None
    
    def makeMove(self, move, player):
        self.grid[move[0]][move[1]] = player
        self.cells[move[0]][move[1]].content = player

    def undoMove(self, move):
        self.grid[move[0]][move[1]] = ""
        self.cells[move[0]][move[1]].content = ""
    
    def checkWinner(self, player):
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

    def isTie(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == "":
                    return False
        return True
    
    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                self.cells[row][col].draw(screen)