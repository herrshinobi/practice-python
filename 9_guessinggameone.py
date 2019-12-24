# Exercise 9: Guessing Game One
print('--------------------------------------------')
print('Guessing Game One')

# Import necessary modules
from sys import *
from random import *

# Generate a random number and establish a count
goldenNum = randint(1, 10)
count = 0

# Nest code in a while loop to keep the game going until told otherwise
while True:
    
# Ask the user to guess the number
    print('--------------------------------------------') 
    guess = int(input('Guess the golden number between 1 and 9!\n'))
    count += 1
    
    if guess == goldenNum:  # Compare the guess to the answer
        print('--------------------------------------------')
        print("You're spot on!")
        print('--------------------------------------------')
        print('You guessed correctly in just {} attempts'.format(count))
    elif guess > goldenNum:
        print('--------------------------------------------')
        print('Your guess is too high, try again!')
        continue
    elif guess < goldenNum:
        print('--------------------------------------------')
        print('Your guess is too low, try again!')
        continue
    
    while True:
        print('--------------------------------------------')
        exitGame = input("Enter 'exit' to end the game, or press enter to continue.\n")
        if exitGame.lower() == 'exit':
            exit()
        else:
            break

