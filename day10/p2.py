with open('input', 'r') as file:
    topo_map = file.read()
    topo_map = topo_map.split('\n')

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

count = 0


def after(cur, row, col):
    global count
    if 0 <= row < len(topo_map) and 0 <= col < len(topo_map[0]):
        if cur == int(topo_map[row][col]) - 1:
            cur += 1
        else:
            return
    else:
        return

    if cur == 9:
        count += 1

    [after(cur, row + dx, col + dy) for dx, dy in directions]


for rowR, row in enumerate(topo_map):
    for columnC, val in enumerate(row):
        if val == '0':
            after(-1, rowR, columnC)

print(count)
