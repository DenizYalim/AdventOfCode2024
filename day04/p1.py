with open("input", "r") as file:
    text = file.readlines()
    text = [row.strip('\n') for row in text]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def checkDirection(c, cc, x, y):
    word = ""
    for _ in range(4):
        while 0 <= x < len(text) and 0 <= y < len(text[0]):
            word += text[x][y]
            x += c
            y += cc
            if word == "XMAS":
                return True

count = 0
for i in range(len(text)):
    for j in range(len(text[0])):
        for direction in directions:
            if checkDirection(direction[0], direction[1], i, j):
                count += 1

print(count)