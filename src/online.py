import pygame
import requests
import time
from src.offline import Offline

class Online(Offline):
    def __init__(self) -> None:
        """
        Constructor for the Online class

        Args:
            None

        Returns:
            None
        """

        super().__init__()
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
        self.horloge = time.time()
    
    def initPlayer(self) -> None:
        """
        Initializes the player

        Args:
            None
        
        Returns:
            None
        """

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
    
    def handleMouseClick(self, pos: tuple[int, int]) -> None:
        """
        Handles the mouse click event

        Args:
            pos (tuple[int, int]): The position of the mouse

        Returns:
            None
        """

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
    
    def isGameOver(self) -> None:
        """
        Checks if the game is over

        Args:
            None

        Returns:
            None
        """

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

    def update(self) -> None:
        """
        Updates the game

        Args:
            None

        Returns:
            None
        """

        self.grid.grid = requests.request("GET", self.urlGame, headers=self.headersPostPut).json()["results"][0]["grid"]
        self.grid.update()
        self.isGameOver()
        self.actualPlayer = requests.request("GET", self.urlGame, headers=self.headersGetDelete).json()["results"][0]["actualPlayer"]
        self.horloge = time.time()
        self.panel.update(self.actualPlayer)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the game

        Args:
            screen (pygame.Surface): The surface to draw the game on (the game window)
        
        Returns:
            None
        """

        if time.time() - self.horloge > 5:
            self.update()
            
        self.grid.draw(screen)
        self.panel.draw(screen)

        if self.gameOver:
            self.line.draw(screen, self.grid.grid)

    def stop(self) -> None:
        """
        Stops the game (delete the players and the game)

        Args:
            None
        
        Returns:
            None
        """

        objectIdList = requests.request("GET", self.urlPlayer, headers=self.headersGetDelete).json()["results"]

        if len(objectIdList) == 0:
            print("No player to delete")
            return
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