

from human import  Human

class Game:
    def __int__(self):
        self.player_one = Human()
        self.player_two

    def run_game(self):

    def welcome_player(self):
        print("")


    def instructions(self):
        print( " Rules for Rock-Paper-Scissors-Lizard-Spock:")
        print(" ")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")

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








    def game_rules(self):













        # Intro
        # Display a welcome message
        # Instructions for play/rules
        # Choose game mode - Single player or Multi player

        # Game Rounds
        # Player one chooses gesture
        # Player two chooses gesture
        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game
        # Display winner of game
        # Prompt to play again? - Not MVP
        pass

    def choose_game_mode(self):
        print("How many players?")
        response = input()
        if response == 2:
            self.player_two = Human()
        else:
            self.player_two = AI()
