from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.gestures = [0, 1, 2, 3, 4]
        self.ai_gesture_list = []

    def choose_gesture(self):
        random_gesture = random.randint(0, len(self.gestures) - 1)
        self.gestures = self.ai_gesture_list[random_gesture]
        ai_input = random_gesture
        self.chosen_gesture_player = int(ai_input)
        self.get_player_name()
