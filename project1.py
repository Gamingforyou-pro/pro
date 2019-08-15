#Hangman Game
#Author Atharva Aka Gamingforyou
import random
import time
import string

print(" This is hangman you should guess what 3 letter word i have chosen")

wordlist  = ['ear','car',
'ace'
]
WordChoice = random.choice(wordlist)
#Check if The word has vowels
for letter in WordChoice:
    if letter in 'aeiou':
        print(letter)
        print("These are the vowels in this word")
else:
    print("There are no vowels in this word")

print("Your Hangman is fully healthy he still has a hat a body and leg")
guess = raw_input("Please enter the whole  word ")
if guess == WordChoice:
    print('You won the word is'+ WordChoice)
else:
    print("You are wrong")
    print("the Hangman lost his hat")
    guess = raw_input("Please enter the whole  word ")
    if guess == WordChoice:
       print('You won the word is'+ WordChoice)
    else:
        print("You are wrong")
        print("the Hangman lost his body")
        guess = raw_input("Please enter the whole  word ")
        if guess == WordChoice:
            print ("You won the word is "+ WordChoice)
        else:
            print("You are wrong and you lost the game the word was" + WordChoice)

