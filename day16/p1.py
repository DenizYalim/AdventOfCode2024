with open("input.txt", "r") as file:
    # a = file.read()
    #print(file.read().split('\n'))
    grid = [list("".join(char for char in line)) for line in (file.read().split('\n'))]

rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'E':
            ei, ej = i, j

# [x][y] = [visited, cost]
# cost düşürülürse visited false olabilir mi?

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North

tileCosts = [[None for _ in range(cols)] for _ in range(rows)] # [i][j] = cost of a tile

def dijsktra(i, j, dir, curCost):
    global tileCosts, estacks, estack # to make tileCosts constant between recursions
    
    if grid[i][j] == '#':
        return
    
    if tileCosts[i][j] == None or tileCosts[i][j] > curCost:
        tileCosts[i][j] = curCost
    else:
        return
    print(grid[i][j] + "  ["+ str(i) +"]["+ str(j) +"] = " + str(tileCosts[i][j]))

    dijsktra(i + directions[dir][0], j + directions[dir][1],dir, curCost + 1)

    for index, (di, dj) in enumerate(directions):
        if dir != index:
            dijsktra(i + di, j + dj, index, curCost + 1001) # yeah not efficient, we are going over same directions
    


# main
# tileCosts[si][sj] = 0
dijsktra(si,sj, 0, 0) # curCost 1'den de başlayabilir
print(tileCosts[ei][ej])
