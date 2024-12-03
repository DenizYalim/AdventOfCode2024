f = open("input", "r")

prompt = f.readlines()
print(prompt)
prompt = ''.join(prompt)

shouldDo = True
sum = 0

for i in range(len(prompt)):
    if prompt[i:i + 4] == "do()":
        shouldDo = True

    if prompt[i:i + 7] == "don't()":
        shouldDo = False

    if prompt[i:i + 4] == "mul(":
        if not ")" in prompt[i + 4:]:
            break
        endIndex = prompt[i + 4:].index(")") + i + 4
        values = prompt[i + 4: endIndex].split(",")

        if len(values) == 2 and values[0].isnumeric() and values[1].isnumeric():
            if shouldDo:
                sum += int(values[0]) * int(values[1])
print(sum)

# todo: These solutions are not very pretty, should learn about regex and solve these using it
