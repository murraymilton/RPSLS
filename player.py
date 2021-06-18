

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.chosen_gesture = ""

    def choose_gesture_player(self):
        gesture_input = input(f"{self.name} Enter your gesture")
        for gesture in self.gestures:
            if gesture_input.lower() == gesture.lower():
                self.chosen_gesture = gesture
                return
        else:
            print("Not a valid input")
            self.choose_gesture_player(self)

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gestures:
            print(each)
            gesture_index += 1




