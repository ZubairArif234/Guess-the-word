from data import data
from helper import functions



def hangMan ():
    word= functions.getRandomWord()
    attempts=6
    guessLetters=[]

    print("Welcome to hangman game!")
    print("guess the name of a flower , in each turn enter a single letter of the word")
   

    while True:
        print("\nyou have {} attemps left".format(attempts))
        print("word {}".format(functions.getHintWord(word,guessLetters)))

        field = input("Enter one letter of the word: ").lower()
       
        if len(field) < 1 or not field.isalpha():
            print("Please enter a alphabet")
            continue
        
        if field in guessLetters:
            print("You have already guessed it.")

        guessLetters.append(field)

        if field not in word:
            attempts -= 1
            print("Incorrect , you loss an attemp") 
            if attempts == 0:
                print("You loss the game , the word was {}".format(word))   
                break
        else:
            print("Bravo! you correct guess")

        if all(alpha in guessLetters for alpha in word):
            print("Awesome! you win the game , the word is {}".format(word))
            break    

if __name__ =="__main__":
    hangMan()