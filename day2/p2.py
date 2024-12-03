input = open("input", "r")

a = input.readlines()
a = [line.strip('\n') for line in a]
a = [line.split() for line in a]

safe = 0

def checkReport(report):
    for i in range(len(report) - 1):
        if not (1 <= abs(int(report[i]) - int(report[i + 1])) <= 3):
            return False

    descendingBool = all(int(report[i]) < int(report[i + 1]) for i in range(len(report) - 1))
    ascendingBool = all(int(report[i]) > int(report[i + 1]) for i in range(len(report) - 1))

    if not (ascendingBool or descendingBool):
        return False

    return True



for report in a:
    if checkReport(report):  # Check if it returns true without modifications

        safe += 1
        continue

    canBeFixed = False
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if checkReport(modified_report):
            canBeFixed = True

            break

    if canBeFixed:
        safe += 1

print(safe)
