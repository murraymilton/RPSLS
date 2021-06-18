from human import Human
from ai import AI


class Game:
    def __int__(self):
        self.player_one = Human()
        self.player_two = None   # gaming logic for selecting the multi player/ or single user against the AI

    def run_game(self):
        self.instructions()

        self.choose_game_mode()

        self.player_one_turn()

        self.player_two_turn()

        self.player_one_chosen_gesture()

        self.player_two_chosen_gesture()

        self.winner_of_round()

        self.game_ends()

        self.winner_announced()

    def instructions(self):    # Create re-select key in the future? MVP is number uno

        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("")
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
        number_players = int(input("How many players for your game?"))
        if number_players == 0 or number_players > 2:
               print("That is not a valid option. There can only be 1 or 2 players")
               if number_players == 2:
                   self.player_two = Human(input("Enter the name of player two"))
               else:
                   self.player_two = AI()

    def players(self, player_one, ai, player_two):
        self.player_one = player_one
        self.ai = ai
        self.player_two = player_two

    def player_one_turn(self):
        print("Player one: Enter your gesture:")
        self.player_one_chosen_gesture = input()

    def player_two_turn(self):
        print("Player two: Enter your gesture:")
        self.player_two_chosen_gesture = input()

    def determining_round_winner(self):
        while self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("There has been a draw!")
            return

        while self.player_one_chosen_gesture == "rock":
            if self.player_two_chosen_gesture == "scissors":
                print("Player one has won! Rock breaks Scissors")
            else:
                print("Player two has won!")
            return

        while self.player_one_turn == "paper":
            if self.player_two_turn == "rock":
                print("Player one has won! Paper covers Rock!")
            else:
                print("Player two has won!")
            return

        while self.player_one_turn == "scissors":
            if self.player_two_turn == "paper":
                print("Player one has won! Scissors cut Paper!")
            else:
                print("player two has won!")
            return
    def player_one_gesture(self):

        self.player_one.show_gesture_options()
        self.player_one.choose_player_gesture()

    def player_two_gesture(self):

        self.player_two.choose_player_gesture()





    def winner_announced(self):
        if self.player_one.score == 3:
            print(f"{self.player_one.name} has won the game!")
            if self.player_two.score == 3:
                print(f"{self.player_two.name} has won the game!")

                self.player_one.chosen_gesture()
                self.player_two.chosen_gesture()






 #                    self.winnner_of_round()
 #
 #                if self.player_one.chosen_gesture == 'rock':
 #                    if self.player_two.chosen_gesture == 'rock':
 #                        print('Its a draw')
 #                    elif self.player_two.chosen_gesture == 'paper':
 #                        self.player_two.score += 1
 #                        print(f"This round goes to {self.player_two}")
 # def winner_of_round(self):
 #        while self.player_one.score <= 3 or self.player_two.score <= 3:
 #
 # def winner_of_round(self):
 #        while self.player_one.score <= 3 or self.player_two.score <= 3:
