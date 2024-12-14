with open("input", "r") as file:
    text = [text.strip('\n') for text in file.readlines()]
    ordering_rules = [text.split('|') for text in text[:text.index('')]]
    updates = [text.split(',') for text in text[text.index(
        '') + 1:]]  # No need to turn string numbers in to ints, they will be just used as symbols

### https://www.youtube.com/watch?v=LA4RiCDPUlI

def follow_rules(update):
    dict = {}
    for i, num in enumerate(update):
        dict[num] = i
    print(dict)

    for num1, num2 in ordering_rules:
        if num1 in dict and num2 in dict and not dict[num1] < dict[num2]:
            return False
    return True

sum = 0
for update in updates:
    if follow_rules(update):
        sum += int(update[len(update)//2])
print(sum)
