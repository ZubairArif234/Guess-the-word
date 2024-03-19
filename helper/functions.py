from data import data
import random

def getRandomWord():
    return random.choice(data.wordlist)


def getHintWord (word,guessedLetters):
    displayWord=""
    for letter in word:
        if letter in guessedLetters:
            displayWord += letter
        else:
            displayWord += "_"
    return displayWord             

