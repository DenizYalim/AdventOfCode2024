with open("input", "r") as file:
    longString = file.read()

longerString = []
for i, char in enumerate(longString):
    if i % 2 != 0:
        [longerString.append(".") for j in range(int(char))]
    else:
        [longerString.append(i // 2) for j in range(int(char))]

left = longerString.index('.')
right = len(longerString) - 1

while (left < right):
    # print(f"{left}: left:{longerString[left]}, {right}:right: {longerString[right]}, {str(longerString)}")
    longerString[left], longerString[right] = longerString[right], longerString[left]
    right -= 1

    while (longerString[right] == '.'):
        right -= 1
    while (longerString[left] != '.'):
        left += 1

goodList = longerString[:longerString.index('.')]  # Get rid of dots

summ = 0
for i, char in enumerate(goodList):
    summ += char * i
print(summ)
