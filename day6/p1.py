with open("input") as file:
    map = file.readlines()
    map = [a.strip('\n') for a in map]
    map = [[a for a in one] for one in map]

for row, line in enumerate(map):
    if '^' in line:
        guard_pos = [row, line.index('^')]


def get_guard_direction(guard_rotation):
    guard_rotation = guard_rotation % 360
    match guard_rotation:
        case 0:
            return [-1, 0]
        case 90:
            return [0, 1]
        case 180:
            return [1, 0]
        case 270:
            return [0, -1]
    return 0


guard_angle = 0
dict = {}  # takes (x,y) key value return boolean about visited status

while 0 <= guard_pos[0] < len(map) and 0 <= guard_pos[1] < len(map[0]):
    dict[(guard_pos[0], guard_pos[1])] = True  # Mark position as visited
    direction_tuple = get_guard_direction(guard_angle)

    requested_x = guard_pos[0] + direction_tuple[0]
    requested_y = guard_pos[1] + direction_tuple[1]
    if 0 <= requested_x < len(map) and 0 <= requested_y < len(map[0]):
        if (map[requested_x][requested_y] != '#'):
            guard_pos[0] = requested_x
            guard_pos[1] = requested_y
        else:
            guard_angle += 90
    else:
        break
print(len(dict))
