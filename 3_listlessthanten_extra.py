# Exercise 3: List Less Than Ten Extra

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

for element in a:
    if element < 5:
        x.append(element)
    else:
        break

print(x)
