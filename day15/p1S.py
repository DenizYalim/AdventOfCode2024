# https://www.youtube.com/watch?v=zYvZS68tPsU

with open("input.txt", "r") as file:
    parts = file.read().strip().split('\n\n') 
    grid = [list(line) for line in parts[0].split('\n')]
    steps = parts[1].replace('\n', "")

directions = {  '<': (0, -1),
                '>': (0,1),
                '^': (-1,0),
                'v': (1,0)}

# Find where the robot is

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '@':
            robot_i, robot_j = i,j
            break

def in_grid(i,j):
    return (i>= 0 and j>= 0) and (i < len(grid) and j < len(grid))

def move_robot(dir):
    global robot_i, robot_j, grid
    new_i, new_j = robot_i + dir[0], robot_j + dir[1]

    if not in_grid(new_i, new_j):
        return
    
    tempi, tempj = robot_i, robot_j

    while in_grid(tempi, tempj):
        tempi += dir[0]
        tempj += dir[1]

        if not in_grid(tempi, tempj):
            break
        
        if grid[tempi][tempj] == '#':
            break
        
        if grid[tempi][tempj] == '.':
            grid[tempi][tempj] = 'O'
            grid[robot_i][robot_j] = '.'
            robot_i, robot_j = robot_i + dir[0], robot_j+ dir[1]
            grid[robot_i][robot_j] = '@'
            break

def printMap(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            print(char,end="")
        print()

for step in steps:
    move_robot(directions[step])


# Calculating GPS
sum = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'O':
            sum += i*100 + j


print(sum)
