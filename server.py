from src.server import Server

host = input("Enter the host: ")
port = int(input("Enter the port: "))
server = Server(host, port)
server.start()