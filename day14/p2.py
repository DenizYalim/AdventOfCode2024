import re

WC_WIDTH = 101
WC_HEIGHT = 103
with open("input", "r") as file:
    robot_pos = file.read().split('\n')
    robot_pos = [list(map(int, re.findall(r"-\d+|\d+", robot))) for robot in robot_pos]
    robot_vel = [(Vx, Vy) for x, y, Vx, Vy in robot_pos]
    print([robot_vel])
    robot_pos = [(x, y) for x, y, Vx, Vy in robot_pos]
    print(robot_pos)


def check_left(x, y, turns_left):
    if turns_left == 0:
        return True
    if (x-1, y+1) not in robot_pos:
        return False
    return check_left(x-1, y+1, turns_left-1)


def check_right(x, y, turns_left):
    if turns_left == 0:
        return True
    if (x+1, y+1) not in robot_pos:
        return False

    return check_left(x+1, y+1, turns_left-1)


def check_tree(x, y, turns_left=10):
    return check_left(x - 1, y + 1, turns_left - 1) and check_right(x + 1, y + 1, turns_left - 1)


tree_found = False
second = 0
while not tree_found:
    second += 1
    for i in range(len(robot_pos)):
        robot_pos[i] = (robot_pos[i][0] + robot_vel[i][0], robot_pos[i][1] + robot_vel[i][1])

    for x, y in robot_pos:
        if x == WC_WIDTH // 2 and y == 0:
            print("try check")
            if check_tree(x, y):
                print(f"Seconds: {second}")
    print(second)
