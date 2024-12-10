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


def checkForLoop(temp_map, guard_pos):
    # print(str(temp_map))
    guard_angle = 0
    dict = {}  # takes ((x,y),(1,0)) as key and Boolean visited
    while 0 <= guard_pos[0] < len(temp_map) and 0 <= guard_pos[1] < len(temp_map[0]):
        direction_tuple = get_guard_direction(guard_angle)

        if ((guard_pos[0], guard_pos[1]), tuple(direction_tuple)) in dict:  # Check for loop
            return True

        dict[((guard_pos[0], guard_pos[1]), tuple(direction_tuple))] = True  # Mark position as visited

        requested_x = guard_pos[0] + direction_tuple[0]
        requested_y = guard_pos[1] + direction_tuple[1]
        if 0 <= requested_x < len(temp_map) and 0 <= requested_y < len(temp_map[0]):
            if temp_map[requested_x][requested_y] != '#':
                guard_pos[0] = requested_x
                guard_pos[1] = requested_y
            else:
                guard_angle += 90
        else:
            return False
    return False


counter = 0

"""
print(map)
map[6][3] = '#'
# print(checkForLoop(map))
if checkForLoop(map):
    counter += 1
print(counter)
"""

for i in range(len(map)):
    print(i)
    for j in range(len(map[0])):
        temp_map = [row[:] for row in map]
        temp_map[i][j] = '#'
        if checkForLoop(temp_map, guard_pos.copy()):
            counter += 1
print(counter)
