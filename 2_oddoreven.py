# Exercise 2: Odd or Even
print('--------------------------------------')
print('Odd or Even')

# Continually asks user for number input until a valid integer is given
while True:
    try:
        print('--------------------------------------')
        num = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Error: Please enter a valid number.')

# Prints message based on whether given integer is odd or even or a multiple of 4
if num % 4 == 0:
    print('--------------------------------------')
    print('This number is a multiple of 4! (mista noises)')
    print('--------------------------------------')
elif num % 2 == 0:
    print('--------------------------------------')
    print('This number is even.')
    print('--------------------------------------')
else:
     print('--------------------------------------')
     print('This number is odd.')
     print('--------------------------------------')
