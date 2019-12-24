# Exercise 7: List Comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Makes a new list for every even number in list a
b = [element for element in a if element % 2 == 0]

# Prints list of even numbers
print(b)
