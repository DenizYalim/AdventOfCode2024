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

                if 0 <= tuple1[0] - dis_x < len(freq_map) and 0 <= tuple1[1] - dis_y < len(freq_map):
                    if freq_map[tuple1[0] - dis_x][tuple1[1] - dis_y] != key:
                        dictAntiNode[(tuple1[0] - dis_x,tuple1[1] - dis_y)] = True

                if 0 <= tuple2[0] - dis_x < len(freq_map) and 0 <= tuple2[1] - dis_y < len(freq_map):
                    if freq_map[tuple2[0] - dis_x][ tuple2[1] - dis_y] != key:
                        dictAntiNode[(tuple2[0] - dis_x, tuple2[1] - dis_y)] = True

                pass
print(len(dictAntiNode))
