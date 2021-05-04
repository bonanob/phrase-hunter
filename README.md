# Project 3: Phrase Hunters

This is a word-guessing console game: "Phrase Hunter." Players try to guess the phrase by inputting individual characters until all of the hidden letters are revealed. Phrases are chosen randomly from a pool. Have fun!

**How to run the project locally:**

If you have python installed, have the folder `phrasehunter` and `app.py` files in a folder and run `app.py`

**Objective:**

The player’s goal is to guess all the letters in a hidden, random phrase. 

**What I've learned:**

- Basic object oriented programming concepts
- Resetting instances of an object
- Working with multiple classes
- Validating user input

**Flow:**

1. At the beginning of the game, the player only sees the number of letters and words in the phrase, represented by an underscore character _ as a placeholder on the screen for a given letter for that phrase.
2. The player inputs a guess for a letter in the phrase.
3. Once a correct letter is guessed, a player cannot guess that letter again.
4. If the guessed letter is in the phrase at least once, the phrase will replace all positions showing the underscore _ with the appropriate letter. All occurrences of that letter are made visible (so if there are 3 A's, all of the A's in the phrase appear at once).
5. If the selected letter is not in the phrase, the number missed increases by one.
6. The player keeps choosing letters until they reveal all the letters in the phrase, or until they make five incorrect guesses.
7. The player is asked to play again.

**Notes:**

- Guesses are validated(only alphabet a-z and A-Z are allowed)
