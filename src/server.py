import socket
import threading
import pickle

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"[+] Server is listening on {self.host}:{self.port}")

        while True:
            client, address = self.server.accept()
            print(f"[+] New connection from {address}")
            print(f"[+] Connection established with {client}")

            if len(self.clients) == 2:
                client.send("Server is full".encode("utf-8"))
                client.close()
                continue
            else:
                if len(self.clients) == 0:
                    client.send("X".encode("utf-8"))    
                    self.clients["X"] = client
                else:
                    client.send("O".encode("utf-8"))
                    self.clients["O"] = client
                    
            threading.Thread(target=self.handleClient, args=(client,)).start()
    
    def handleClient(self, client):
        while True:
            data = client.recv(1024)
            if data:
                print(f"[*] {client.getpeername()}: {data}")
                self.broadcast(data, client)

    def broadcast(self, data, client):
        for name in self.clients:
            if self.clients[name] != client:
                self.clients[name].send(data)

    def stop(self):
        print("[-] Server is stopping")
        self.server.close()