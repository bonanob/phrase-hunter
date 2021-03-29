class Phrase:
    """All active phrases(currently being guessed) is an instance of this class.
    """

    def __init__(self, phrase):
        """
            phrase (str): phrase itself.
            correct_letters (list): correct player guesses are appended to keep track
        """
        self.phrase = phrase.lower()
        self.correct_letters = []

    def display(self):
        """Displays each letter of the phrase as _ with white spaces in between.
        """
        for letter in self.phrase:
            if letter in self.correct_letters:
                print(letter, end=" ")
            else:
                if letter == " ":
                    print(" ", end="")
                else:
                    print("_", end=" ")
        else:
            print()

    def check_letter(self, guess_letter):
        """Checks if the player guesses are in the phrase, and appends the correct guesses in [correct_letters]

        Args:
            guess_letter (str): An player inputted guess

        Returns:
            bool: only returns True, if it is a correct guess.
        """
        for letter in self.phrase.replace(" ", ""):
            if letter == guess_letter:
                self.correct_letters.append(guess_letter)
                print("'{}' was found!".format(guess_letter))
                return True
        else:
            print("'{}' was not found.".format(guess_letter))

    #
    # def check_letter_message(self, guess_letter):
    #     """Shows the result of check_letter().
    #
    #     Args:
    #         guess_letter (str): A player inputted guess
    #     """
    #     if self.check_letter(guess_letter):
    #     else:

    def check_complete(self):
        """Checks if all of the letters are guessed right.

        Returns:
            bool: True(all letters in the phrase are guessed right.), False(There are more letters to guess.)
        """
        if set(self.phrase.replace(" ", "")) == set(self.correct_letters):
            return True
        return False
