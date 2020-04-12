""""""

from random import sample
import socket

from cards import (SUSPECTS, WEAPONS, PLACES, SERIALIZED)


HOST = '127.0.0.1'
PORT = 65432


class GameServer:
    def __init__(self, suspects, places, weapons, num_players):
        self.suspects = sample(suspects, len(suspects))
        self.places = sample(places, len(places))
        self.weapons = sample(weapons, len(weapons))
        self.num_players = num_players
        self.connected = []

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)

        self.chosen = self.choose()
        self.merged_cards = self.suspects + self.places + self.weapons
        self.merged_cards = sample(self.merged_cards, len(self.merged_cards))

        self.main_loop()

    def choose(self):
        return list(map(list.pop, [self.suspects, self.places, self.weapons]))

    def deal_cards(self):
        i = 0
        while len(self.merged_cards) > 0:
            card = self.merged_cards.pop()
            self.connected[i].send(SERIALIZED[card])
            i = (i+1) % self.num_players

    def main_loop(self):
        while len(self.connected) < self.num_players:
            (clientsocket, address) = self.socket.accept()
            print(str(address) + " connected")
            self.connected.append(clientsocket)
        self.deal_cards()


if __name__ == '__main__':
    GameServer(SUSPECTS, PLACES, WEAPONS, 4)
