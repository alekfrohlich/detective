""""""


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

CARDS = SUSPECTS + WEAPONS + PLACES
SERIALIZED = {card:str(i).encode('utf-8') for i, card in enumerate(CARDS)}
DESERIALIZED = {str(i).encode('utf-8'):card for i, card in enumerate(CARDS)}