from player import Player


class Human(Player):
    def __init__(self):
        self.gestures = ""
        self.set_name()

    def set_name(self):
        self.name = input("Enter your player name")