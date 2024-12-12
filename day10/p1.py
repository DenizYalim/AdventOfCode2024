with open('input', 'r') as file:
    topo_map = file.read()
    topo_map = topo_map.split('\n')

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

print(topo_map)


"""
def after0(cur, row, col):
    print(f"cur: {cur}, row: {row}, col: {col}")
    if 0 <= row < len(topo_map) and 0 <= col < len(topo_map[0]):
        print("asd")
        if cur == int(topo_map[row][col]) - 1:
            cur += 1
        else:
            return False
    else:
        return False

    if cur == 9:
        return True

    return any([after0(cur, row + dx, col + dy) for dx, dy in directions])
    """


def after(cur, row, col, nineList):
    # print(f"cur: {cur}, row: {row}, col: {col}")
    if 0 <= row < len(topo_map) and 0 <= col < len(topo_map[0]):
        if cur == int(topo_map[row][col]) - 1:
            cur += 1
        else:
            return
    else:
        return

    if cur == 9:
        if (row, col) not in nineList:
            nineList.append((row, col))

    for dx, dy in directions:
        after(cur, row + dx, col + dy, nineList)


def after0(cur, row, col):
    nineList = []
    after(cur, row, col, nineList)
    return len(nineList)


count = 0
for rowR, row in enumerate(topo_map):
    for columnC, val in enumerate(row):
        if val == '0':
            # print("asd")
            """
            if after0(-1, rowR, columnC):
                count += 1
                """
            """"""
            count += after0(-1, rowR, columnC)

print(count)