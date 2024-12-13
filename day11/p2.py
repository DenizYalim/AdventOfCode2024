with open("input", "r") as file:
    stones = file.read()
    stones = stones.split(' ')
    stones = [int(stone) for stone in stones]

def getDigit(number):
    return len(str(number))


def stoneAfterBlink(stone): # Should take 1 stone return a list of the output for 1 blink


def countForStoneAfterBlinks(stone, stepSize): # Should take 1 stone, should return len(list) after n steps



def findCountForList(stones, stepSize): # Should run recur1 for each stone, sum up the returns
    count = 0
    for stone in stones:
        count += countForStoneAfterBlinks(stone, stepSize)
    return count

stepSize = 5
print(findCountForList(stones, stepSize))
