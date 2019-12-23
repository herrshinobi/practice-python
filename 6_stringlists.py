# Exercise 6: String Lists

# Ask user to input a word
string = input('Please enter a word: ')

# Assign the length of the word to a variable and establish a count
length = len(string)
count = 0

# For every character in the word, check if it is equal to its opposing character
for c in string:
    if c == string[-(string.index(c)+1)]:        
        count += 1 # If it is then the count increases by 1
    else:
        continue
        
# If the count is equal to the length of the word, the word is a palindrome
if count == length:
    print('This word is a palindrome!')
else:
    print('This word is not a palindrome...')
                         
