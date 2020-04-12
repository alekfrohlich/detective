""""""

import socket

from cards import DESERIALIZED


HOST = '127.0.0.1'
PORT = 65432


class GameClient:
    def __init__(self, host):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

        self.main_loop()

    def main_loop(self):
        while True:
            data = self.socket.recv(1)
            if not data:  # received all cards
                break
            card = DESERIALIZED[data]
            print(card)

if __name__ == '__main__':
    print("Please input the server's IP address")
    GameClient(input())
