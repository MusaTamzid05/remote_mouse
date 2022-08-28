import socket
from pynput import mouse



class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket()
        self.host = socket.gethostname()

        self._init_server()

    def _init_server(self):
        self.server_socket.bind((self.host, self.port))
        self.queue = []

    def run(self):

        try:
            server_address = socket.gethostbyname(self.host)
            print(f"[*] Server Listening {server_address}:{self.port}")
            self.server_socket.listen(1)
            conn, address = self.server_socket.accept()

            print(f"connect to : {address[0]}")

            while True:

                if len(self.queue) == 0:
                    continue

                message = self.queue[0]
                self.queue = []

                print(message)
                conn.send(message.encode())
        except KeyboardInterrupt:
            print("[*] Closing server")
            self.server_socket.close()





server = Server(port = 5000)

def on_move(x, y):
    global server

    if len(server.queue) > 0:
        return

    server.queue.append(f"mouse_pos={x},{y}")

if __name__ == "__main__":
    listener = mouse.Listener(on_move = on_move)
    listener.start()
    server.run()




