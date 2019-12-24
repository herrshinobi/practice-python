# Exercise 8: Rock Paper Scissors

# Import required package
import sys

# Nest code in a while loop to allow the game to restart
while True:

# Asks for each player's decision    
    play1 = input('Player 1, choose Rock, Paper or Scissors: ')
    play2 = input('Player 2, choose Rock, Paper or Scissors: ')

# Compares each input
    if play1.lower() == play2.lower():
        print('This round is a tie...')
    elif play1.lower() == 'rock' :
        if play2.lower() == 'scissors':
            print('Player 1 wins this round!')
        else:
            print('Player 2 wins this round!')
    elif play1.lower() == 'paper' :
        if play2.lower() == 'rock':
            print('Player 1 wins this round!')
        else:
            print('Player 2 wins this round!')
    elif play1.lower() == 'scissors' :
        if play2.lower() == 'paper':
            print('Player 1 wins this round!')
        else:
            print('Player 2 wins this round!')

# Allows the players to decide to continue
# Nested in a while loop to ensure player enter's a valid option
    while True:
        playAgain = input('Play again? (y/n)')
    
        if playAgain == 'y':
            break
        elif playAgain == 'n':
            sys.exit()
        else:
            print('Please enter a valid option.')
            continue
