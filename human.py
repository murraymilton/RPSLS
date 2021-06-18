from player import Player


class Human(Player):
    def __init__(self, name):
        self.gestures = ""
        super().__init__(name)

    def set_name(self):
        self.name = input("Enter player name")