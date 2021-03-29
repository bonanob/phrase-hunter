import random
import string

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        """
        missed: number of wrong guesses
        phrases: pool of phrases to randomly choose from
        active_phrase: the phrase currently being guessed
        guesses: all the guesses by the player 
        """
        self.missed = 0
        self.pharses = ["Once in a blue moon", "When pigs fly",
                        "A piece of cake", "Break a leg", "Jupyter notebook"]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        """Calls the welcome method, creates the game loop. Players are asked to play again.
        """
        self.welcome()
        self.get_random_phrase()
        while not self.active_phrase.check_complete():
            self.active_phrase.display()
            self.get_guess()
            if self.validate_input(self.guesses[-1]):
                self.missed += 1
                print("You have {} out of 5 lives.".format(5 - self.missed))
            elif not self.active_phrase.check_letter(self.guesses[-1]):
                self.missed += 1
                print("You have {} out of 5 lives.".format(5 - self.missed))
            print()
            if self.missed >= 5:
                break
        self.game_over()
        for _ in range(10):
            replay = str(input("Play again? (y/n) "))
            if replay.lower() in ('y', 'n'):
                break
            else:
                print("Please choose between 'y' or 'n': ")
        if replay.lower() == 'y':
            self.reset()
            self.start()
        else:
            print("Bye.")

    def reset(self):
        """Resets the instance, if a players chooses to play again.
        """
        self.__init__()

    def get_random_phrase(self):
        """Pulls a random phrase from phrases
        """
        self.active_phrase = Phrase(random.choice(self.pharses))

    def welcome(self):
        """A warm welcoming message at the beginning of the game.
        """
        print()
        print("-----------------------------------------------")
        print("Welcome to the wonderful game of Phrase Hunters!", end="\n")
        print("-----------------------------------------------")

    def get_guess(self):
        """Takes a player guess.
        """
        self.guesses.append(input("Please guess a letter: "))

    def validate_input(self, user_input):
        """Validates a player guess. Only alphabets a-z and first time guesses are allowed.

        Args:
            user_input (str): A player guess

        Returns:
            bool: False if it isn't anything other than what is allowed. True if a player tries to guess a letter
            multiple times.
        """
        if user_input not in string.ascii_lowercase or len(user_input) > 1:
            print("Please enter one letter from a to z.")
            return False
        elif len(self.guesses) >= 2 and self.guesses.count(user_input) > 1:
            print("You've already tried {}".format(user_input))
            return True

    def game_over(self):
        """Shows a win/lose message at the end of the game.
        """
        if self.active_phrase.check_complete():
            print("Congratulations! You won!")
        else:
            print("Out of luck. You lost.")
