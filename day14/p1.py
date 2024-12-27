import re

WC_WIDTH = 101
WC_HEIGHT = 103
SECONDS = 100
print(f"1-2={1 % 10}")
with open("input", "r") as file:
    robot_pos = file.read().split('\n')
    robot_pos = [map(int, re.findall(r"-\d+|\d+", robot)) for robot in robot_pos]
    robot_pos = [((x + Vx * SECONDS) % WC_WIDTH, (int(y) + int(Vy) * SECONDS) % WC_HEIGHT) for x, y, Vx, Vy in
                 robot_pos]
    print(robot_pos)

# q1, q2, q3, q4 = [], [], [], []
q1, q2, q3, q4 = 0, 0, 0, 0
for x, y in robot_pos:
    if x == WC_WIDTH // 2 or y == WC_HEIGHT // 2:
        continue

    x_upper = x < WC_WIDTH // 2
    y_upper = y < WC_HEIGHT // 2

    if (x_upper, y_upper) == (True, True):
        q1 += 1
    elif (x_upper, y_upper) == (True, False):
        q3 += 1
    elif (x_upper, y_upper) == (False, True):
        q2 += 1
    elif (x_upper, y_upper) == (False, False):
        q4 += 1

print(f"Robot Count: {len(robot_pos)} . q1: {q1}, q2: {q2}, q3: {q3}, q4: {q4}, mult: {q1 * q2 * q3 * q4}")
