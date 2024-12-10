with open("input", "r") as file:
    rows = file.readlines()
    rows = [row.strip('\n') for row in rows]
    answers, numbers = zip(*[row.split(":") for row in rows])
    answers = [int(a) for a in answers]
    numbers = [number.strip(' ') for number in numbers]
    numbers = [number.split(' ') for number in numbers]
    numbers = [[int(i) for i in sublist] for sublist in numbers]


def checkSideToSide(answer, numbers, operators, leftToRight=False):  # [12,24,24] [*,+]
    numbers = numbers.copy()  # Create a local copy of numbers
    operators = operators.copy()  # Create a local copy of operators

    if leftToRight:
        i = 0  # Left to Right
    else:
        i = len(operators) - 1

    while len(numbers) != 1:
        if operators[i] == '*':
            numbers[i + 1] = numbers[i] * numbers[i + 1]
        elif operators[i] == '+':
            numbers[i + 1] = numbers[i] + numbers[i + 1]
        else:  # Concatenation
            numbers[i + 1] = int(str(numbers[i]) + str(numbers[i + 1]))  # Funny solution, I know
        numbers.pop(i)
        operators.pop(i)

        if i != 0:  # If not leftToRight
            i -= 1

    if answer == numbers[0]:
        return True
    return False


def generate_permutations(operators, current, n):
    if len(current) == n:
        return [''.join(current)]  # Return completed permutation

    permutations = []
    for op in operators:
        current.append(op)
        permutations += generate_permutations(operators, current, n)
        current.pop()

    return permutations


sum = 0
for i, answer in enumerate(answers):
    operators = ['+', '*', '|']
    checksOut = False
    permutations = generate_permutations(operators, [], len(numbers[i]) - 1)
    for perm in permutations:
        if checkSideToSide(answer, numbers[i], list(perm), True):
            checksOut = True
            break
        if checkSideToSide(answer, numbers[i], list(perm), False):
            checksOut = True
            break
    if checksOut:
        print(str(i) + " of "+ str(len(answers))+":  "+ str(answer))
        sum += answer

print(sum)  # The right answer for my input was: 162042343638683, which is just diabolically huge
