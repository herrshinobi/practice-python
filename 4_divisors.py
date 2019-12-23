# Exercise 4: Divisors

# Asks user for number
num = int(input('Please enter a number: '))

# Generates list containing integers from 1 to given numeber
x = range(1, (num + 1))

# Generate empty list for divisors
y = []

# Checks every number in x as a divisor of the given number
for elem in x:

# If the given number is 1, a special message is returned
    if num == 1:
        print('The only divisor of 1 is 1.')

# If it is a divisor it is added to a new list  
    elif num % elem == 0:      
        y.append(elem)
    else:
        continue

# Outputs all the divisors of the given number
print('The divisors of ' + str(num) + ' are ' + str(y)+ '.')
