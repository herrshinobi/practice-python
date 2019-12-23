# Exercise 6: String Lists

# Ask user to input a word
string = input('Please enter a word: ')

# If the string reversed is equal to its normal value, it is a palindrome
if string.lower() == string[::-1].lower():
    print('This word is a palindrome!')
else:
    print('This word is not a palindrome...')
                         
