import socket

class Client:
    def __init__(self, host, port):
        self.client_socket = socket.socket()
        try:
            self.client_socket.connect((host, port))
            self.running = True
        except ConnectionRefusedError as e:
            print(e)
            self.running = False

    def listen(self):
        while self.running:
            message = self.client_socket.recv(1024).decode()
            result = self._process_input(message)
            if result is None:
                continue
            print(result)

    def _process_input(self, message):
        result = {}
        if "mouse_pos" in message:
            try:

                mouse_data = message.split("=")
                mouse_data = mouse_data[1].split(",")
                result["x"] = int(mouse_data[0])
                result["y"] = int(mouse_data[1])

                return result
            except ValueError as e:
                print(e)
                return None

        else:
            print(message)



if __name__ == "__main__":
    client = Client(host = "192.168.1.3", port = 5000)
    client.listen()
