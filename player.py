

class Player:
    def __init__(self):
        self.name = ""
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.chosen_gesture = ""

    def choose_gesture_player(self):
        gesture_input = input(f"{self.name} Enter your gesture")
        for gesture in self.gesture_list:
            if gesture_input.lower() == gesture.lower():
                self.chosen_gesture = gesture
                return
        else:
            print("Not a valid input")
            self.choose_gesture_player()

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gesture_list:
            print(each)
            gesture_index += 1




