# Project 3: Phrase Hunters

Objective:
Guess the letters of a phrase until you win(guess all the letters) or lose(run out of lives)


Flow of the game:

1. A random phrase (within a list) is chosen and each letter of the phrase is displayed as an underscore character
   placeholders, _.

2. Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase.
   If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

3. A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose)
   .

4. If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses
   incorrectly five times, a losing screen appears.

5. Players are asked, if they want to play again.


Notes:

- Guesses are validated(only alphabet a-z and A-Z are allowed)
