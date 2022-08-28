import socket
from pynput import mouse
from threading import Thread
import time



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
click_count = 0

def on_move(x, y):
    global server


    for item in server.queue:
        if "mouse_pos" in item:
            continue

    server.queue.append(f"mouse_pos={x},{y}")

def helper_click():
    global click_count
    time.sleep(0.2)
    if click_count == 1:
        server.queue.append("single_left")
    elif click_count == 2:
        server.queue.append("double_left")


    click_count = 0


def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1

    if click_count ==  1:
        thread = Thread(target = helper_click)
        thread.start()


if __name__ == "__main__":
    listener = mouse.Listener(on_move = on_move, on_click = on_click)
    listener.start()
    server.run()




