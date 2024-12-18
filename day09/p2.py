with open("input", "r") as file:
    longString = file.read()
longerString = []
for i, char in enumerate(longString):
    if i % 2 != 0:
        [longerString.append(".") for j in range(int(char))]
    else:
        [longerString.append(i // 2) for j in range(int(char))]
# print(longerString)

numbers = sorted(set(longerString) - {'.'}, reverse=True)

for i, number in enumerate(numbers):
    print(f"{i}: out of {len(numbers)}")
    countOfNumber = longerString.count(number)
    for i in range(len(longerString) - countOfNumber + 1):
        # print("b")
        if i > longerString.index(number):
            break
        if all(longerString[i+j] == '.' for j in range(countOfNumber)):
            for _ in range(countOfNumber):
                # print("c")
                longerString[longerString.index(number)] = '.'
            # longerString = longerString[:len(longerString) - countOfNumber] # will cut last digits THIS WONT WORK
            for j in range(countOfNumber):
                # print("d")
                longerString[i+j] = number
            break
print(longerString)
a = sum([i*c for i,c in enumerate(longerString) if c != '.'])

print(a)