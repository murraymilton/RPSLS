

from human import Human
from ai import AI

import random

class Game:
    def __int__(self):
        self.

    def run_game(self):
        print( " Rules for Rock-Paper-Scissors-Lizard-Spock:")

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



    def __init__(self):
        self.player_one = Human()
        self.player_two = None
        pass


    def game_rules(self):



def game_









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
