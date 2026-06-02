
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description

Create the game setup so that the program selects a random secret word from a predefined list and displays progress to the player.

#### Requirements
Completed program should:

- Use a list of possible secret words.
- Randomly select one word at the start of the game.
- Display the hidden word progress with blanks for unguessed letters, for example: `_ _ _ _ _`.
- Show the list of letters guessed so far.

### 🛠️ Letter Guessing and Game Flow

#### Description

Implement the main Hangman game loop so players can guess letters, track remaining attempts, and win or lose correctly.

#### Requirements
Completed program should:

- Accept letter guesses from the player.
- Reveal correct letters in the hidden word when guessed.
- Decrease remaining attempts for incorrect guesses.
- End the game when the word is fully guessed or attempts run out.
- Print a win message if the player guesses the word, or a lose message if they run out of attempts.
