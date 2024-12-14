with open("input", "r") as file:
    stones = file.read()
    stones = stones.split(' ')
    stones = [int(stone) for stone in stones]


def getDigit(number):
    return len(str(number))


def stoneAfterBlink(stone):  # Should take 1 stone return a list of the output for 1 blink
    if stone == 0:
        return False, [1]

    if getDigit(stone) % 2 == 0:
        half = 10 ** (getDigit(stone) / 2)
        left = stone // half
        right = stone - left * half
        return True, [int(left), int(right)]

    return False, [stone * 2024]


dp = {}  # (number: int, stepsLeft: int) -> numberOfStonesCreatedAfterTurns : int


def countForStoneAfterBlinks(stone, stepSize):  # Should take 1 stone, should return len(list) after n steps
    if (stone, stepSize) in dp:
        return dp[(stone, stepSize)]

    if stepSize == 0:
        return 1

    addition, newList = stoneAfterBlink(stone)

    result = countForStoneAfterBlinks(newList[0], stepSize - 1)

    if addition:
        result += countForStoneAfterBlinks(newList[1], stepSize - 1)

    dp[(stone, stepSize)] = result

    return result


def findCountForList(stones, stepSize):  # Should run recur1 for each stone, sum up the returns
    count = 0
    for stone in stones:
        count += countForStoneAfterBlinks(stone, stepSize)
    return count


stepSize = 75
print(findCountForList(stones, stepSize))
