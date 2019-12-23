# Exercise 1: Character Input

from datetime import *

currentYear = datetime.now()

print('----------------------------------------')
print('Character Input')
# Asks the user for relevant input
print('----------------------------------------')
name = input('Please enter your name: ')
currentAge = int(input('Please enter your age: '))

# Calculates the year the user will turn 100
hundredYear = 100 + (currentYear.year - currentAge)

# Assigns addressed message to a variable
message = (name + ', you will turn 100 in ' + str(hundredYear) + '.')

# Prints out addressed message
print('----------------------------------------')
print(message)

# Asks user how many times message should be repeated
print('----------------------------------------')
count = int(input('Please enter a random numebr: '))

# Prints message said number of times on separate lines
print('----------------------------------------')
print(((message+'\n') * count)[:-1])
print('----------------------------------------')
