class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.correct_letters = []

    def display(self):
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
        for letter in self.phrase.replace(" ", ""):
            if letter == guess_letter:
                self.correct_letters.append(guess_letter)
                return True

    def check_letter_message(self, guess_letter):
        if self.check_letter(guess_letter):
            print("'{}' was found!".format(guess_letter))
        else:
            print("'{}' was not found.".format(guess_letter))

    def check_complete(self):
        if set(self.phrase.replace(" ", "")) == set(self.correct_letters):
            return True
        return False
