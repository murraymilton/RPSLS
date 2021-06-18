from human import Human
from ai import AI


class Game:
    def __int__(self):
        self.player_one = ""
        self.player_two = ""

    def run_game(self):
        self.instructions()

        self.choose_game_mode()

        self.player_one_chosen_gesture()

        self.player_two_chosen_gesture()

        self.game_start()

        self.winner_announced()

        self.another_round()   # Create re-play key option?

    def instructions(self):

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
        self.player_one.choose_gesture_player()

    def player_two_chosen_gesture(self):
        self.player_two.choose_gesture_player()

    def game_start(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            if self.player_one.score == 3 or self.player_two == 3:
                self.winner_announced()

            if self.player_one.chosen_gesture.lower() == self.player_two.chosen_gesture.lower():
                print("There has been a draw!")





    def winner_announced(self):
        if self.player_one.score == 3:
            print(f"{self.player_one.name} has won the game!")
            if self.player_two.score == 3:
                print(f"{self.player_two.name} has won the game!")


    def another_round(self):
        pass




