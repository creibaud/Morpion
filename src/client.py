import socket
import threading
import pickle

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = None

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enemyMove = []
    
    def start(self):
        self.client.connect((self.host, self.port))
        print("[+] Connection established")
        self.name = self.client.recv(1024).decode("utf-8")

        threading.Thread(target=self.handleServer).start()
    
    def handleServer(self):
        while True:
            data = pickle.loads(self.client.recv(1024))
            
            if data:
                self.enemyMove.append(data)

    def send(self, data):
        self.client.send(pickle.dumps(data))
    
    def stop(self):
        print("[-] Connection is closing")
        self.client.close()