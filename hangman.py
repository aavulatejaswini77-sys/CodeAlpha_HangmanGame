
import random

# List of predefined words
words = ["python", "apple", "school", "coding", "mobile"]

# Randomly select a word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the hidden word.")

# Game loop
while wrong_guesses < max_attempts:

    display_word = ""

    # Display guessed and hidden letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Attempts left:", max_attempts - wrong_guesses)

# Losing condition
if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
