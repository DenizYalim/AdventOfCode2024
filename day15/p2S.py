# https://www.youtube.com/watch?v=aCqtVmSSkUs

with open('input.txt', 'r') as file:
    top, bottom = file.read().split('\n\n')

expansion = {'#': '##', '.': '..', '@': '@.', 'O': '[]'}

grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]

moves = bottom.replace('\n', '')

r, c = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            r, c = i, j
            break

for move in moves:
    dr = {'^': -1, 'v': 1}.get(move, 0)
    dc = {'<': -1, '>': 1}.get(move, 0)
    
    if dr == 0 and dc == 0:  # invalid move
        continue
        
    targets = [(r, c)]
    go = True


    i = 0
    while i < len(targets):
        cr, cc = targets[i]
        nr = cr + dr
        nc = cc + dc
        
        if (nr, nc) in targets: 
            i += 1
            continue
        
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[nr])):
            go = False
            break
        
        char = grid[nr][nc]
        if char == '#':
            go = False
            break
        
        if char == '[':
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
        
        if char == ']':
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        
        i += 1
    
    if not go:
        continue
    

    box_chars = {}
    for br, bc in targets[1:]:
        box_chars[(br, bc)] = grid[br][bc]
    
  
    grid[r][c] = '.'
    grid[r + dr][c + dc] = '@'
    
    
    for br, bc in targets[1:]:
        grid[br][bc] = '.'
    
   
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = box_chars[(br, bc)]
    
    r += dr
    c += dc

print(sum(100*r + c for r in range(len(grid)) for c in range(len(grid)) if grid[r][c] == '['))