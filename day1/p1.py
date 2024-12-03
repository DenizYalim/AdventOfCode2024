import re

f_input = open("input", "r")

a = f_input.readlines()
a = [line.strip('n') for line in a]

l1 = []
l2 = []

for line in a:
    col1, col2 = map(int, line.split())
    l1.append(col1)
    l2.append(col2)


totalSeparation = 0
for i in range(len(l1)):
    totalSeparation += abs(min(l1) - min(l2))
    l1.remove(min(l1))
    l2.remove(min(l2))

print("total = " + str(totalSeparation))
f_input.close()

"""
    Inefficiencies for the above code:
        1) Looking for min() each time is really costly, a better way would be to sort each
        list in ascending order once, and then go over the lists simultaneously.
        * This would also remove the need to use remove()
"""
