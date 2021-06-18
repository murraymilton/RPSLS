from player import Player

import random


class AI(Player):
    def __init__(self):
        self.set_ai_name()
        self.gestures = ""
        self.ai_gesture_list = []

    def set_ai_name(self):
        self.name = "Obi-Wan Kenobi"

    def choose_gesture(self):
        random_gesture = random.randint(0, len(self.gestures) - 1)
        ai_gesture_list = self.ai_gesture_list[random_gesture]
        self.gestures = ai_gesture_list

