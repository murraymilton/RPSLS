from player import Player


class Human(Player):
    def __init__(self, name):
        self.gesture_list = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]
        self.chosen_gesture = " "
        super().__init__()
        self.set_name()

    def show_gesture_options(self):
        gesture_index = 0
        for each in self.gesture_list:
            print(each)
            gesture_index += 1

    def choose_gesture(self):
       gesture_input = input("Pick your gesture")
       for gesture_ in self.gesture_list:
           if gesture_input.lower() == gesture.lower():
              print(f"You picked {gesture}")
              self.chosen_gesture = gesture