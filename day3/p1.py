f = open("input", "r")

input = f.readlines()
print(input)
input = ''.join(input)


sum = 0
for i in range(len(input)):
    if input[i:i+4] == "mul(":
        if not ")" in input[i+4:]:
            break
        endIndex = input[i + 4:].index(")") + i+4
        values = input[i+4: endIndex].split(",")

        if len(values) == 2 and values[0].isnumeric() and values[1].isnumeric():
            sum += int(values[0])* int(values[1])
print(sum)

""" GPT's solution with Regex
import re
# search = r"mul\\((\\d{1,3}),\\d{1,3})\\)"
search = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(search, input)

sum = sum(int(a)*int(b) for a,b in matches)
print(sum)
"""