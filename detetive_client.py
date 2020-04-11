""""""

import socket

from cards import DESERIALIZED


HOST = '127.0.0.1'
PORT = 65431


class GameClient:
    def __init__(self, server_ip):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

        self.main_loop()

    def main_loop(self):
        for i in range(18):
            card = DESERIALIZED[self.socket.recv(1)]
            print(card)

if __name__ == '__main__':
    print("Please input the server's IP address")
    GameClient(input())
