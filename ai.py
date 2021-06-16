from player import Player
import random


class AI(Player):
    def __init__(self):
        self.ai_gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock" ]
        self.chosen_gesture = " "
        super().__init__()
        self.ai_name()

        # Randomly generate name from a list of characters
    def ai_name(self):
            pass

    def choose_gesture(self):
        random_gesture = random.randint(0, len(self.ai_gesture_list) - 1)
        ai_gesture = self.ai_gesture_list[random_gesture]
        print(f"Your opponent is {ai_gesture}")
        self.ai_chosen_gesture = ai_gesture
