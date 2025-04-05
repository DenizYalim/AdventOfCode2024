with open("input.txt", "r") as file:
    inputt = file.read()
 
moves = inputt.split('\n')[-1]
map_start = inputt.split('\n')[:-2]
map_start = [[a for a in line] for line in map_start]


def printMap(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            print(char,end="")
        print()

def getAt(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == '@':
                return (x,y)

def moveF(directions, map):
    x,y = getAt(map)
    cur_x = x+directions[0]
    cur_y = y+directions[1]
    while(map[cur_x][cur_y] == 'O'):
        cur_x = cur_x+directions[0]
        cur_y = cur_y+directions[1]

    if(map[cur_x][cur_y] == '#'):
        # No movement is done
        return
    
    map[cur_x][cur_y] = 'O'
    map[cur_x + directions[0]][cur_y + directions[1]] = '@'
    return


if __name__ == '__main__':
    printMap(map_start)
    for turn, move in enumerate(moves):
        match move:
            case "<":
                moveF((-1,0),map_start)
            case ">":
                moveF((1,0),map_start)
            case "^":
                moveF((0,-1),map_start)
            case "v":
                moveF((0,1),map_start)

    printMap(map_start)

    
