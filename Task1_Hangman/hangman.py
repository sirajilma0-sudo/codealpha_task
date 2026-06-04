import random

# List of predefined words
words = ["python", "computer", "network", "coding", "program"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_guesses:

    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_guesses - wrong_guesses)

# If all chances are used
if wrong_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
