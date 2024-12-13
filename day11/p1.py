with open("input", "r") as file:
    stones = file.read()
    stones = stones.split(' ')
    stones = [int(stone) for stone in stones]
print(stones)

def getDigit(number):
    return len(str(number))

def returnStone(index):
    if stones[index] == 0:
        stones[index] = 1
        return False

    if getDigit(stones[index])%2 == 0:
        half = 10**(getDigit(stones[index])/2)
        left = stones[index]//half
        right = stones[index] - left*half
        stones[index] = int(left)
        stones.insert(index+1, int(right))
        return True

    stones[index] = stones[index]*2024
    return False

stepSize = 25
for step in range(stepSize):
    index = 0
    for _ in range(len(stones)):
        if returnStone(index): # lol
            index += 1
        index += 1
print(len(stones))