from player import Player


class Human(Player):
    def __init__(self):
        self.chosen_gestures = " "
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = input("Enter your player name")