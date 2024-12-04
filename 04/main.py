directions = [[0, 1], [0, -1], [1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
grid = []
total1 = 0

def checkM(i, j, direction):
    if not 0 <= i < 140 or not 0 <= j < 140:
        return
    if grid[i][j] == 'M':
        checkA(i+direction[0], j+direction[1], direction)

def checkA(i, j, direction):
    if not 0 <= i < 140 or not 0 <= j < 140:
        return
    if grid[i][j] == 'A':
        checkS(i+direction[0], j+direction[1], direction)

def checkS(i, j, direction):
    if not 0 <= i < 140 or not 0 <= j < 140:
        return
    global total1
    if grid[i][j] == 'S':
        total1 += 1

def task1():
    input_file = open("input.txt")
    for line in input_file.readlines():
        grid.append(line.strip())
    for i in range(140):
        for j in range(140):
            if grid[i][j] == 'X':
                for direction in directions:
                    checkM(i+direction[0], j+direction[1], direction)
    return total1

def task2():
    total2 = 0
    for i in range(1,140-1):
        for j in range(1,140-1):
            if grid[i][j] == 'A':
                if grid[i-1][j-1] == 'M':
                    if grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S' and grid[i+1][j+1] == 'S':
                        total2 += 1
                    if grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S' and grid[i+1][j+1] == 'S':
                        total2 += 1

                if grid[i-1][j-1] == 'S':
                    if grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M' and grid[i+1][j+1] == 'M':
                        total2 += 1
                    if grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M' and grid[i+1][j+1] == 'M':
                        total2 += 1
    return total2

if __name__ == '__main__':
    print(task1())
    print(task2())