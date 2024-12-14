f = open('input', 'r')

a = f.readlines()

a = [line.strip('\n') for line in a]

l1 = []
l2 = []

for line in a:
    col1, col2 = map(int, line.split())
    l1.append(col1)
    l2.append(col2)

l1.sort()
l2.sort()

score = 0
for i in range(len(l1)):
    if l1[i] in l2:
        starting_index = l2.index(l1[i])
        j = 0
        count = 0
        while starting_index + j < len(l2):
            if l1[i] == l2[starting_index + j]:
                count += 1
            j += 1
        score += l1[i] * count

print(score)

"""
    --GPT's witty solution--
    
    
    from collections import Counter

    with open('input', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    l1, l2 = zip(*(map(int, line.split()) for line in lines))

    l2_counts = Counter(l2)

    score = sum(num * l2_counts[num] for num in l1)

    print(score)
"""
