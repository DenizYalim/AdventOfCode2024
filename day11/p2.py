with open("input", "r") as file:
    stones = file.read()
    stones = stones.split(' ')
    stones = [int(stone) for stone in stones]

def getDigit(number):
    return len(str(number))

dictForStone = {}
def returnStone(index, array):
    if array[index] in dictForStone:
        return dictForStone[array[index]]

    if array[index] == 0:
        array[index] = 1
        return False

    if getDigit(array[index])%2 == 0:
        half = 10**(getDigit(array[index])/2)
        left = array[index]//half
        right = array[index] - left*half
        array[index] = int(left)
        array.insert(index+1, int(right))
        return True

    array[index] = array[index]*2024
    return False

def recur1(array, stepSize):
    for step in range(stepSize):
        for _ in range(len(array)):
            index = 0
            if returnStone(index, array):  # lol
                index += 1
            index += 1

totalCount = 0
def findStoneCountForStone(stone, stepSize):
    global totalCount
    array = []
    array.append(stone)
    recur1(array, stepSize)
    totalCount += len(array)

stepSize = 5
findStoneCountForStone(125, stepSize)
print(totalCount)