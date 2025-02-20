#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return letter == word[spot]

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ["*"] * 5
    word_used = list(word)

    # Check for correct letters in the correct spot (uppercase)
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot):
            feedback[spot] = myLetter.upper()
            word_used[spot] = None  # Mark as used

    # Check for correct letters in the wrong spot (lowercase)
    for spot in range(5):
        myLetter = myGuess[spot]
        if feedback[spot] == "*":
            if myLetter in word_used:
                feedback[spot] = myLetter.lower()
                word_used[word_used.index(myLetter)] = None  # Mark as used

    return "".join(feedback)

def main():
    # Pick a random word from the list of all words
    with open("words.txt", 'r') as wordFile:
        content = wordFile.read().strip()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)

    guessNum = 1
    while guessNum <= 6:
        # Ask user for their guess
        validWord = False
        while not validWord:
            guess = input("Enter Guess: ").strip().lower()
            if guess not in wordList:
                print("Word not in list. Try again.")
            elif len(guess) != 5:
                print("Please enter a 5-letter word.")
            else:
                validWord = True

        # Provide feedback
        feedback = rateGuess(guess, todayWord)
        print(feedback)

        if guess == todayWord:
            print(f"You are correct!! {guessNum} Tries!")
            return  # Exit the function if guessed correctly

        guessNum += 1

    print("Game over! The word was", todayWord)

if __name__ == '__main__':
    main()

