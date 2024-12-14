with open("input", "r") as file:
    plot_map = file.read()
    plot_map = plot_map.split('\n')
# print(plot_map)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = {}  # (row, col) -> boolean


def recursive(row, col, letter):  # returns (borderLength, area)
    borderLength, area = 0, 1
    if not (0 <= row < len(plot_map) and 0 <= col < len(plot_map[0])):
        return 1, 0

    if plot_map[row][col] != letter:
        return 1, 0

    if (row, col) in visited:
        return 0, 0

    visited[(row, col)] = True

    for dx, dy in directions:
        a2, b2 = recursive(row + dx, col + dy, plot_map[row][col])
        borderLength += a2
        area += b2

    return borderLength, area


cost = 0
a, b = 0, 0
for i in range(len(plot_map)):
    for j in range(len(plot_map[0])):
        if not (i, j) in visited:
            x, d = recursive(i, j, plot_map[i][j])
            a = x
            b = d
            print(f"{i, j}, {plot_map[i][j]} : {b, a}")
            # visited.clear()
            cost += b * a

print(cost)
