with open("input", "r") as file:
    stones = file.read()
    stones = stones.split(' ')
    stones = [int(stone) for stone in stones]

def getDigit(number):
    return len(str(number))


def stoneAfterBlink(stone): # Should take 1 stone return a list of the output for 1 blink
    if stone == 0:
        return [1]

    if getDigit(stone)%2 == 0:
        half = 10 ** (getDigit(stone) / 2)
        left = stone // half
        right = stone - left * half
        return [int(left), int(right)]
    return [stone*2024]

def countForStoneAfterBlinks(stone, stepSize): # Should take 1 stone, should return len(list) after n steps
    count = 0
    outpt = []
    outpt.append(stone)
    for step in range(stepSize):
        tempList = []
            for



def findCountForList(stones, stepSize): # Should run recur1 for each stone, sum up the returns
    count = 0
    for stone in stones:
        count += countForStoneAfterBlinks(stone, stepSize)
    return count

stepSize = 5
print(findCountForList(stones, stepSize))
