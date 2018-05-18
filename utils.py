import os

def checkWin(underscore, secretWordList):
    """Returns True if user's guessed all letters correctly"""
    return underscore == secretWordList

def cls():
    os.system("clear")
    # os.system("cls") # FOR WINDOWS