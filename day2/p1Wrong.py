input = open("input", "r")

a = input.readlines()
a = [line.strip('\n') for line in a]
a = [line.split() for line in a]

safe = 0

for report in a:
    safeBool = True
    sum = 0  # for checking if all descending or ascending
    for i in range(len(report) - 1):

        if not (1 <= abs(int(report[i]) - int(report[i + 1])) <= 3):
            safeBool = False
            print("failByIncrement: " + str(report))
            break

        if abs(sum) > abs(sum + int(report[i]) - int(
                report[i + 1])):  # This breaks if sum = 1 and after getting -3 dif, sum is now = 2
            safeBool = False
            print("failByDescendAscend: " + str(report))
            break
        sum += sum + int(report[i]) - int(report[i + 1])

    if safeBool:
        print("Success: " + str(report))
        safe += 1

print(safe)

# This solution is wrong, due to how it checks if all are descending or ascending.(Gpt wasn't able to find the error)
# And out of the 1000 input lines only 1 was wronged because of this wrong solution.
