# Exercise 5: List Overlap

# For two sets of lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
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
