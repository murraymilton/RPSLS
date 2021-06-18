class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0
        self.chosen_gesture_player = ""

    def choose_gesture_player(self):
        gesture_input = input(f"{self.name} Enter your gesture")
        for gesture in self.gestures:
            if gesture_input.lower() == gesture.lower():
                self.chosen_gesture_player = gesture
                return

        else:
            print("Not a valid input")
            self.chosen_gesture_player()  #Test to see if the recall during user (validation) works?

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gestures:
            print(each)
            gesture_index += 1




