with open("input", "r") as file:
    text = file.readlines()
    text = [row.strip('\n') for row in text]

directions = [[(1, 1), (-1, -1)], [(-1, 1), (1, -1)]]


def checkXMAS(x, y):
    word = text[x][y]

    valid = True
    for i in range(len(directions)): # Goes over lists in the directions list
        for j in range(len(directions[0])): # Goes over the tuples
            if 0 <= x + directions[i][j][0] < len(text) and 0 <= y + directions[i][j][1] < len(text[0]): # If index out of bounds doesn't occur
                word += text[x + directions[i][j][0]][y + directions[i][j][1]] # Add current letter
        if word != "AMS" and word != "ASM": # If word created is invalid
            valid = False
        else:
            word = text[x][y]

    return valid

count = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        if checkXMAS(i, j):
            count += 1

print(count)
