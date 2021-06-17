class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.chosen_gesture_player = 0

    def choose_gesture_player(self):
        return int(self.chosen_gesture_player)
    def get_player_name(self):
        self.gesture_name = self.gestures[self.chosen_gesture_player]




