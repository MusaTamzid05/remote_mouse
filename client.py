import socket

class Client:
    def __init__(self, host, port):
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))

    def test(self):
        while True:
            message = self.client_socket.recv(4096).decode()
            print(message)


if __name__ == "__main__":
    client = Client(host = "192.168.1.3", port = 5000)
    client.test()
