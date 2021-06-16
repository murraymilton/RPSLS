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

        # if gesture_input.lower() == "help":
        #     # lets show user the instructions again or if the wrong input is entered
        #     pass
        # elif inp.lower() == "exit":
        #     clear()
        #     break
        # elif inp.lower() == "rock":
        #     player_move = 0
        # elif inp.lower() == "paper":
        #     player_move = 1
        # elif inp.lower() == "scissors":
        #     player_move = 2
        # elif inp.lower() == "lizard":
        #     player_move = 3
        # elif inp.lower() == "spock":
        #     player_move = 4



