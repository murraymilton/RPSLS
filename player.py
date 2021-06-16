class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.chosen_gesture = ""
        self.gestures = ["rock", "paper", "scissors", "lizard", "Spock"]

    def choose_gesture_player(self):
        gesture_input = input("Enter your move : ")
        for gesture in self.gestures:
            if gesture_input.lower() == gesture.lower():
               print(f"{gesture_input}")





