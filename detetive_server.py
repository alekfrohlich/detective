""""""

from random import sample
import socket


HOST = '127.0.0.1'
PORT = 65431

SUSPECTS = [
    "Col. Mustard",
    "Prof. Plum",
    "Rev. Green",
    "Mrs. Peacock",
    "Miss Scarlet",
    "Mrs. White",
]

WEAPONS = [
    "Knife",
    "Candlestick",
    "Revolver",
    "Rope",
    "Lead Pipe",
    "Wrench",
]

PLACES = [
    "Hall",
    "Lounge",
    "Dinning Room",
    "Kitchen",
    "Ball Room",
    "Conservatory",
    "Billiard Room",
    "Library",
    "Study",
]


class GameServer:
    def __init__(self, suspects, places, weapons):
        self.suspects = sample(suspects, len(suspects))
        self.places = sample(places, len(places))
        self.weapons = sample(weapons, len(weapons))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)

        self.chosen = self._choose()
        self.merged_cards = self.suspects + self.places + self.weapons
        self.merged_cards = sample(self.merged_cards, len(self.merged_cards))

        self.main_loop()

    def _choose(self):
        return list(map(list.pop, [self.suspects, self.places, self.weapons]))

    def _push_cards(self):
        pass

    def main_loop(self):
        # FIXME: Wait for N connections before distributting cards
        (clientsocket, address) = self.socket.accept()
        print(str(address) + " connected")
        while len(self.merged_cards) > 0:
            card = self.merged_cards.pop().encode('utf-8')
            print(card)
            clientsocket.sendall(card)


if __name__ == '__main__':
    GameServer(SUSPECTS, PLACES, WEAPONS)
