with open("input", "r") as file:
    text = [text.strip('\n') for text in file.readlines()]
    ordering_rules = [text.split('|') for text in text[:text.index('')]]
    updates = [text.split(',') for text in text[text.index(
        '') + 1:]]  # No need to turn string numbers in to ints, they will be just used as symbols

def follow_rules(update):
    dict = {}
    for i, num in enumerate(update):
        dict[num] = i
    # print(dict)

    for num1, num2 in ordering_rules:
        if num1 in dict and num2 in dict and not dict[num1] < dict[num2]:
            return False
    return True

def topological_sort(update):
    important_rules = []
    for a, b in ordering_rules:
        if a in update and b in update:
            important_rules.append([a, b])

    new_update = []

    while len(update) != 0:
        for char in update:
            if all(char not in sublist[0] for sublist in important_rules):
                new_update.insert(0, char)
                important_rules = [sublist for sublist in important_rules if char not in sublist]
                update.remove(char)
    # print(new_update)
    return new_update


sum = 0
for update in updates:
    if not follow_rules(update):
        list = topological_sort(update)
        sum += int(list[len(list)//2])
print(sum)
