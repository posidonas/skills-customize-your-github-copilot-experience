
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python strings, loops, and user input. Learn to model game logic, manage state, and handle user interactions.

## 📝 Tasks

### 🛠️ Set Up Game Words and Display

#### Description
Create the foundation for the Hangman game by setting up a word list and implementing the display logic to show the player's progress.

#### Requirements
Completed program should:

- Maintain a predefined list of words to guess
- Randomly select a word from the list at game start
- Display the current progress using underscores (e.g., `_ _ _ _`)
- Track which letters have been guessed


### 🛠️ Implement Guessing and Feedback

#### Description
Add the core guessing mechanism where players can input letter guesses and receive feedback about their guesses.

#### Requirements
Completed program should:

- Accept single-letter guesses from the player
- Check if the guessed letter is in the word
- Update the display to reveal correct guesses
- Track incorrect guesses remaining (limit of 6-10 attempts)
- Provide feedback for each guess (correct/incorrect)


### 🛠️ Add Win/Lose Conditions and Game Flow

#### Description
Complete the game by implementing win/lose logic and a full playable game flow with user prompts and game ending conditions.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (win condition)
- End the game when incorrect guesses are exhausted (lose condition)
- Display appropriate win/lose messages
- Show the final word when the game ends
- Allow the player to play again if desired
- Display game statistics (attempts used, accuracy)
