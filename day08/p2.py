with open("input", "r") as file:
    freq_map = file.read()
    freq_map = freq_map.split('\n')


dictAntenna = {}  # Takes char, holds vector for all positions
dictAntiNode = {}  # Takes x,y tuple returns boolean value of an antiNode is there or not

for i, row in enumerate(freq_map):  # Taking note of the positions of every antenna
    for j, val in enumerate(row):
        if val != '.':
            if val in dictAntenna:
                dictAntenna[val].append((i, j))
            else:
                dictAntenna[val] = [(i, j)]


for key in dictAntenna:
    for tuple1 in dictAntenna[key]:
        for tuple2 in dictAntenna[key]:  # We go over repeated tuples of tuples with this. ex: (1,1)x(8,8) and (8,8)x(1,1)
            if tuple1 != tuple2:
                dis_x = tuple1[0] - tuple2[0]
                dis_y = tuple1[1] - tuple2[1]

                temp_x = dis_x
                temp_y = dis_y

                while 0 <= tuple1[0] - dis_x < len(freq_map) and 0 <= tuple1[1] - dis_y < len(freq_map):
                    if freq_map[tuple1[0] - dis_x][tuple1[1] - dis_y] != key:
                        dictAntiNode[(tuple1[0] - dis_x, tuple1[1] - dis_y)] = True
                    dis_x += temp_x
                    dis_y += temp_y
                dis_x = temp_x
                dis_y = temp_y

                while 0 <= tuple2[0] - dis_x < len(freq_map) and 0 <= tuple2[1] - dis_y < len(freq_map):
                    if freq_map[tuple2[0] - dis_x][ tuple2[1] - dis_y] != key:
                        dictAntiNode[(tuple2[0] - dis_x, tuple2[1] - dis_y)] = True
                    dis_x += temp_x
                    dis_y += temp_y

                pass

for i, tuple in enumerate(dictAntiNode):
    if freq_map[tuple[0]][tuple[1]] == '.' or True:
        freq_map[tuple[0]] = list(freq_map[tuple[0]])  # Convert the string to a list
        freq_map[tuple[0]][tuple[1]] = '#'
        freq_map[tuple[0]] = ''.join(freq_map[tuple[0]])

"""for j in range(len(freq_map)):
    for i in range(len(freq_map[0])):
        print(freq_map[j][i], end='')
    print()"""

icerdekiler = 0
for row in freq_map:
    for a in row:
        if a != '.' and a != '#':
            icerdekiler+= 1

print(len(dictAntiNode) + icerdekiler)


