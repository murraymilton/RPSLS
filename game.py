from human import Human
from ai import AI


# while self.player_one.score <= 3 or self.player_two.score <= 3:
#     self.player_one.chosen_gesture()
#     self.player_two.chosen_gesture()
#     self.winnner_of_round()
class Game:
    def __int__(self):
        self.player_one = Human()
        self.player_two = None   # gaming logic for selecting the multi player/ or single user against the AI

    def run_game(self):
        self.instructions()

        self.choose_game_mode()

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

# User Input validation: Conditionals for for counting the number of rounds won(while? for?
    def choose_game_mode(self):
        number_players = int(input("How many players for your game?"))
        if number_players == 0 or number_players > 2:
               print("That is not a valid option. There can only be 1 or 2 players")
               self.choose_game_mode()
               if number_players == 2:
                   self.player_two = Human(input("Enter the name of player two"))
               else:
                    self.player_two = AI("R2D2")

    def winner_of_round(self):
        if self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'rock':
                print('Its a draw')
            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.score += 1
                print(f"This round goes to {self.player_two}")





    # Once the game has ended: Keep or just announce all in the winner announcement?


        # after concluding the games end will announce the winner of the game with visual score bord using
        # a simple column row board.



        # Choose game mode - Single player or Multi player

        # Game Rounds
        # Player one chooses gesture
        # Player two chooses gesture
        # Determine winner of round, winner's score increases
        # Loop to continue gameplay until best of three occurs

        # End Game

        # Prompt to play again? - Not MVP


    def winner_announced(self):
        if self.player_one.score == 2:
            print(f"{self.player_one.name} has won the game!")
            if self.player_two.score == 2:
                print(f"{self.player_two.name} has won the game!")