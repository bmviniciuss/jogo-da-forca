# Input handlers


def getSecretWord():
    """Return a secret word."""
    while True:
        secretWord = str(input("Type a secret word: ")).lower()
        if secretWord.isalpha():
            return secretWord
        else:
            print("Type a valid word.")
            print()


def getGuess():
    """Return the user's guess """
    while True:
        guess = input("Guess a letter(or a word): ").lower()
        if guess.isalpha() and len(guess) > 0:
            return guess
        else:
            print("Type a valid input.")
            print()


def playAgain():
    return binaryQuestion("Do you want to play again? (y/n): ")

def playAlone():
    return binaryQuestion("Are you gonna play by yourself? (y/n): ")

def binaryQuestion(question):
    """Returns True if user say 'y', or False otherwise"""
    while True:
        res = input(question).lower()
        if res == 'y':
            return True
        elif res == 'n':
            return False
        else:
            print("Type a valid input!!")
            print()
