with open("input", "r") as file:
    plot_map = file.read()
    plot_map = plot_map.split('\n')
# print(plot_map)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = {}  # (row, col) -> boolean


def recursive(row, col, letter):  # returns (borderLength, area)
    cornerCount, area = 0, 1
    if not (0 <= row < len(plot_map) and 0 <= col < len(plot_map[0])):
        return 0, 0, True

    if plot_map[row][col] != letter:
        return 0, 0, True

    if (row, col) in visited:
        return 0, 0, False

    visited[(row, col)] = True

    uC, uA, up = recursive(row - 1, col + 0, plot_map[row][col])  # todo remove uC uA stuff
    dC, dA, down = recursive(row + 1, col + 0, plot_map[row][col])
    lC, lA, left = recursive(row - 0, col - 1, plot_map[row][col])
    rC, rA, right = recursive(row - 0, col + 1, plot_map[row][col])

    if (up and left) or (up and right):
        cornerCount += 1
    if (down and left) or (down and right):
        cornerCount += 1


    cornerCount += uC + dC + lC + rC
    area += uA + dA + lA + rA

    return cornerCount, area, False


cost = 0
a, b = 0, 0
for i in range(len(plot_map)):
    for j in range(len(plot_map[0])):
        if not (i, j) in visited:
            x, d, gereksiz = recursive(i, j, plot_map[i][j])
            a = x
            b = d
            print(f"{i, j}, {plot_map[i][j]} : {b, a}")
            # visited.clear()
            cost += b * a

print(cost)
