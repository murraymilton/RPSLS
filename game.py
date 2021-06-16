from human import Human
from ai import AI


class Game:
    def __int__(self):
        self.player_one = Human()
        self.player_two = None   # gaming logic for selecting the multi player/ or single user against the AI

    def run_game(self):
        self.instructions()

        self.game_selected_mode()

        self.player_one.chosen_gesture()

        self.player_two.chosen_gesture()

        self.game_ends()

        self.winner_announced()

    def instructions(self):    # Create re-select key in the future? MVP is number uno

        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("")
        print(" The rules for Rock-Paper-Scissors-Lizard-Spock:")
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


# User Input validation: Conditionals for for counting the number of rounds won(while? for?

    def game_selected_mode(self):
        game_mode = input(" Would you like to play  ")
        pass

    def game_ends(self):
        print("The game has ended ")
        pass

    # Once the game has ended: Keep or just announce all in the winner announcement?
    def winner_announced(self):
        pass
        # after concluding the games end will announce the winner of the game with visual score bord using
        # a simple column row board.

















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
