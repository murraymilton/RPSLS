






# """
# Classes - EACH IN OWN FILE
# Game
# Player
# AI(Player)
# Human(Player)
# """


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
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
