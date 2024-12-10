with open("input", "r") as file:
    rows = file.readlines()
    rows = [row.strip('\n') for row in rows]
    answers, numbers = zip(*[row.split(":") for row in rows])
    answers = [int(a) for a in answers]
    numbers = [number.strip(' ') for number in numbers]
    numbers = [number.split(' ') for number in numbers]
    numbers = [[int(i) for i in sublist] for sublist in numbers]


def checkSideToSide(answer, numbers, operators):  # [12,24,24] [*,+]
    temp_answer, temp_numbers, temp_op = answer, numbers.copy(), operators.copy()
    i = 0 # Left to Right
    while len(numbers) != 1:
        if operators[i] == '*':
            numbers[i + 1] = numbers[i] * numbers[i + 1]
        else:
            numbers[i + 1] = numbers[i] + numbers[i + 1]
        numbers.pop(i)
        operators.pop(i)

    # print(numbers[0])
    if answer == numbers[0]:
        return True

    i = len(temp_op) - 1 # Left to Right
    while len(temp_numbers) != 1:
        print(str(len(temp_numbers)) + "   " + str(i))
        print(temp_op)
        if temp_op[i] == '*':
            temp_numbers[i + 1] = temp_numbers[i] * temp_numbers[i + 1]
        else:
            temp_numbers[i + 1] = temp_numbers[i] + temp_numbers[i + 1]
        temp_numbers.pop(i)
        temp_op.pop(i)
        i-= 1

    print(temp_numbers)
    if answer == temp_numbers[0]:
        return True
    return False


for i, answer in enumerate(answers):
    pass

ans = 292
# num =[11, 6, 16, 20] # Left to Right
num = [20, 16, 6, 11] # Right to Left
op = ['+', '*', '+']
print(checkSideToSide(ans, num, op))