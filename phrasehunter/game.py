import random
import string

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.pharses = ["Once in a blue moon", "When pigs fly", "A piece of cake", "Break a leg", "Jupyter notebook"]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.get_random_phrase()
        while not self.active_phrase.check_complete():
            self.active_phrase.display()
            self.get_guess()
            if not self.validate_input(self.guesses[-1]):
                self.active_phrase.check_letter_message(self.guesses[-1])
            if not self.active_phrase.check_letter(self.guesses[-1]):
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
        self.__init__()

    def get_random_phrase(self):
        self.active_phrase = Phrase(random.choice(self.pharses))

    def welcome(self):
        print()
        print("-----------------------------------------------")
        print("Welcome to the wonderful game of Phrase Hunter!", end="\n")
        print("-----------------------------------------------")

    def get_guess(self):
        self.guesses.append(input("Please guess a letter: "))

    def validate_input(self, user_input):
        if user_input not in string.ascii_lowercase or len(user_input) > 1:
            print("Please enter one letter from a to z.")
            return False

    def game_over(self):
        if self.active_phrase.check_complete():
            print("Congratulations! You won!")
        else:
            print("Out of luck. You lost.")
