from human import Human
from ai import AI
from player import Player


class Game:
    def __int__(self):
        self.player_one = ""
        self.player_two = ""

    def run_game(self):
        self.instructions()

        self.choose_game_mode()

        self.player_one_chosen_gesture()

        self.player_two_chosen_gesture()

        self.winner_of_round()

        self.winner_announced()

        self.another_round()

    def instructions(self):    # Create re-select key in the future? MVP is number uno

        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("______________________________________________")
        print("The rules for Rock-Paper-Scissors-Lizard-Spock:")
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

    def choose_game_mode(self):
        number_players = input("How many players for your game?")
        number_players = int(number_players)
        if number_players == 0 or number_players > 2:
            print("That is not a valid option. There can only be 1 or 2 players")
        if number_players == 2:
            self.player_one = Human()
            self.player_two = Human()
        elif number_players == 1:
            self.player_one = Human()
            self.player_two = AI()
        else:
            self.choose_game_mode()

    def player_one_chosen_gesture(self):
        self.player_one.show_gesture_options()
        self.player_one.chosen_gesture()

    def player_two_chosen_gesture(self):
        self.player_two_chosen_gesture()

    def winner_of_round(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            if self.player_one.score == 3 or self.player_two == 3:
                self.winner_announced()

            if self.player_one.chosen_gesture.lower() == self.player_two.chosen_gesture.lower():
                print("There has been a draw!")
                return



    # def game_ends(self):
    #         pass

      #Revise conditional statement to increment each round once a winner is announced.

    # Revise conditional statement to increment each round once a winner is announced.

    # Winner total will be resolved by using the increment of +=1 each round a user is announced

    def winner_announced(self):
        if self.player_one.score == 3:
            print(f"{self.player_one.name} has won the game!")
            if self.player_two.score == 3:
                print(f"{self.player_two.name} has won the game!")



    def another_round(self):
        pass




