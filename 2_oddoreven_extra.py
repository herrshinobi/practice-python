# Exercise 2: Odd or Even (Extra)
print('--------------------------------------')
print('Odd or Even: Extra')

# Continually asks user for number and check input until a valid integer is given
while True:
    try:
        print('--------------------------------------')
        num1 = int(input('Please enter a number: '))
        print('--------------------------------------')
        check1 = int(input('Please enter the number you would like to divide by: '))
        break    
    except ValueError:
        print('Error: Please enter a valid number.')

# Prints message based on whether given number is divisible by the given check
def numCheck(num, check):
    if num % check == 0:
        print('--------------------------------------')
        print(num, 'divides evenly into', str(check) + '.')
        print('--------------------------------------')
    else:
         print('--------------------------------------')
         print(num, 'does not divide evenly into', str(check) + '.')
         print('--------------------------------------')

numCheck(num1, check1)
