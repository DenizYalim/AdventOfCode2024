input = open("input", "r")

a = input.readlines()
a = [line.strip('\n') for line in a]
a = [line.split() for line in a]

safe = 0

for report in a:
    safeBool = True
    for i in range(len(report) - 1):

        if not (1 <= abs(int(report[i]) - int(report[i + 1])) <= 3):
            safeBool = False
            print("failByIncrement: " + str(report))
            break

    descendingBool = all(int(report[i]) < int(report[i+1]) for i in range(len(report) -1))
    ascendingBool = all(int(report[i]) > int(report[i + 1]) for i in range(len(report)-1))

    if not (ascendingBool or descendingBool):
        print("failByDescending: "+ str(report))
        safeBool = False


    if safeBool:
        print("Success: "+str(report))
        safe += 1

print(safe)
