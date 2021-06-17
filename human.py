from player import Player


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture_player(self):
       gesture_index = 0
       for gesture in self.gestures:
           print(f"Select your {gesture_index} for {gesture}")
           gesture_index += 1
           human_input = input("Select your gesture.")
           self.chosen_gesture_player = int(human_input)
           self.get_player_name()