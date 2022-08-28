import socket

class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket()
        self.host = socket.gethostname()

        self._init_server()

    def _init_server(self):
        self.server_socket.bind((self.host, self.port))


    def run(self):
        server_address = socket.gethostbyname(self.host)
        print(f"[*] Server Listening {server_address}:{self.port}")
        self.server_socket.listen(1)
        conn, address = self.server_socket.accept()

        print(f"connect to : {address[0]}")
        conn.send("Connected".encode())






if __name__ == "__main__":
    server = Server(port = 5000)
    server.run()




