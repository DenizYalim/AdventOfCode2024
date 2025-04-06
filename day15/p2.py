def printMap(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            print(char,end="")
        print()


with open("input.txt", "r") as file:
    parts = file.read().strip().split('\n\n') 
    grid = [list(line) for line in parts[0].split('\n')]
    steps = parts[1].replace('\n', "")

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            
            if char == '.':
                grid[i].insert(j, '.')
            elif char == '#':
                grid[i].insert(j, '#')
            elif char == 'O':
                grid[i][j] = '['
                grid[i].insert(j, ']')
            elif char == '@':
                grid[i].insert(j+1,'.') 
            # i+=1
            j+=1
    # printMap(grid)

directions = {  '<': (0, -1),
                '>': (0,1),
                '^': (-1,0),
                'v': (1,0)}

# Find where the robot is

def get_robot_ij():
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j])
            if grid[i][j] == '@':
                print("ASDSADSAD")
                return [i,j]

def in_grid(i,j):
    return (i>= 0 and j>= 0) and (i < len(grid) and j < len(grid))

def move_in_j(i,j, dir):
    if grid[i][j] == '.':
        return True
    if grid[i][j] == '#':
        return False
    
    # it is a box
    if grid[i][j] == '[':
        kutu_sol_i, kutu_sol_j = i, j
        kutu_sag_i, kutu_sag_j = i, j + 1
    else:
        kutu_sol_i, kutu_sol_j = i, j - 1
        kutu_sag_i, kutu_sag_j = i, j  

    sol_bool = move_in_j(kutu_sol_i, kutu_sol_j, dir)
    sag_bool = move_in_j(kutu_sag_i, kutu_sag_j, dir)
    to_move = sol_bool and sag_bool

    if not to_move:
        return False
    grid[kutu_sol_i][kutu_sol_j] = '.'
    grid[kutu_sag_i][kutu_sag_j] = '.'
        
    grid[kutu_sol_i + dir[0]][kutu_sol_j + dir[1]] = '['
    grid[kutu_sag_i + dir[0]][kutu_sag_j + dir[1]] = ']'
    return True
    
def move_in_i(i, j, dir):
    if grid[i][j] == '#':
        return False
    
    if grid[i][j] == '.':
        grid[i][j] = grid[i -dir[0]][j -dir[1]]
        return True
    
    ok_mi = move_in_i(i+ dir[0], j + dir[1], dir)

    if ok_mi:
        if grid[i][j] == '@':
            grid[i][j] = '.'
        else:
            grid[i][j] = grid[i -dir[0]][j -dir[1]]
    return ok_mi
         

def move(step):
    # global robot_i, robot_j, grid
    a = get_robot_ij()
    ri, rj = a[0], a[1]
    if step == '<' or step == '>':
        b = move_in_i(ri, rj, directions[step])
    else:
        b = move_in_j(ri, rj, directions[step])
    
    if b:
        grid[ri][rj] = '.'
        ri, rj = ri + directions[step][0], rj + directions[step][1]
        grid[ri][rj] = '@'
    
for step in steps:
    move(step)


# Calculating GPS
sum = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '[':
            sum += i*100 + j


print(sum)
