import requests
import time
from src.grid import Grid
from src.panel import Panel
from src.line import Line

class Online:
    def __init__(self):
        self.grid = Grid()
        self.panel = Panel()
        self.line = Line()
        self.urlGame = "https://parseapi.back4app.com/classes/Morpion"
        self.urlPlayer = "https://parseapi.back4app.com/classes/Player"
        self.headersPostPut = {
            "X-Parse-Application-Id": "yRpYaPlAZ6so2uzzv1b1FFBBvOnxSabC5rOTql5N",
            "X-Parse-REST-API-Key": "qKMEiimFjxaLVq2DQaFEpoEWxXKqo5Uvtij4WEZn",
            "Content-Type": "application/json"
        }
        self.headersGetDelete = {
            "X-Parse-Application-Id": "yRpYaPlAZ6so2uzzv1b1FFBBvOnxSabC5rOTql5N",
            "X-Parse-REST-API-Key": "qKMEiimFjxaLVq2DQaFEpoEWxXKqo5Uvtij4WEZn"
        }

        self.player = self.initPlayer()
        self.actualPlayer = "X"
        self.gameOver = False
        self.horloge = time.time()
    
    def initPlayer(self):
        response = requests.request("GET", self.urlPlayer, headers=self.headersGetDelete).json()["results"]
        if len(response) == 0:
            requests.request("POST", self.urlPlayer, headers=self.headersPostPut, json={"symbol": "X"})
            return "X"
        elif len(response) == 1:
            requests.request("POST", self.urlPlayer, headers=self.headersPostPut, json={"symbol": "O"})
            return "O"
        else:
            print("The game is already full")
            exit()

    def handleMouseHover(self, pos):
        self.grid.handleMouseHover(pos, self.gameOver)
    
    def handleMouseClick(self, pos):
        if self.grid.handleMouseClick(pos, self.player, self.gameOver) and self.player == self.actualPlayer:
            self.isGameOver()
            self.actualPlayer = "O" if self.actualPlayer == "X" else "X"

            objectId = requests.request("GET", self.urlGame, headers=self.headersGetDelete).json()["results"][0]["objectId"]
            data = {
                "grid": self.grid.grid,
                "actualPlayer": self.actualPlayer
            }
            requests.request("PUT", self.urlGame + "/" + objectId, headers=self.headersPostPut, json=data)
            self.panel.update(self.actualPlayer)
    
    def isGameOver(self):
        winner = self.grid.checkWinner(self.actualPlayer)
        if winner:
            self.panel.winner = self.actualPlayer
            self.gameOver = True
        else:
            tie = self.grid.isTie()
            if tie:
                self.panel.tie = True
                self.gameOver = True

        requests.request("PUT", self.urlGame, headers=self.headersPostPut, json={"gameOver": self.gameOver})

    def update(self):
        self.grid.grid = requests.request("GET", self.urlGame, headers=self.headersPostPut).json()["results"][0]["grid"]
        self.grid.update()
        self.isGameOver()
        self.actualPlayer = requests.request("GET", self.urlGame, headers=self.headersGetDelete).json()["results"][0]["actualPlayer"]
        self.horloge = time.time()
        self.panel.update(self.actualPlayer)

    def draw(self, screen):
        if time.time() - self.horloge > 5:
            self.update()
            
        self.grid.draw(screen)
        self.panel.draw(screen)

        if self.gameOver:
            self.line.draw(screen, self.grid.grid)

    def stop(self):
        objectIdList = requests.request("GET", self.urlPlayer, headers=self.headersGetDelete).json()["results"]

        if len(objectIdList) == 0:
            print("No player to delete")
            exit()
        else:
            for i in range(2):
                requests.request("DELETE", self.urlPlayer + "/" + objectIdList[i]["objectId"], headers=self.headersGetDelete)
        
        objectId = requests.request("GET", self.urlGame, headers=self.headersGetDelete).json()["results"][0]["objectId"]
        data = {
            "grid": [["", "", ""], ["", "", ""], ["", "", ""]],
            "actualPlayer": "X",
            "gameOver": False
        }
        requests.request("PUT", self.urlGame + "/" + objectId, headers=self.headersGetDelete, json=data)
        exit()