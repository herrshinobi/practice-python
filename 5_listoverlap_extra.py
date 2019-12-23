# Exercise 5: List Overlap Extra

# Import required modules

from random import *

# For two random sets of lists
a = [randrange(1, 100) for i in range(100)]
b = [randrange(1, 100) for i in range(100)]
c = []

# Check if an element from a is in b and not c
for elem in a:
    if elem in b and elem not in c:

# If it is then it is added to list c
        c.append(elem)
    else:
        continue

# Check if an element from b is in a and not c
for elem in b:
    if elem in a and elem not in c:

# If it is then it is added to list c
        c.append(elem)
    else:
        continue

# Print the contents of list c
print(c)
