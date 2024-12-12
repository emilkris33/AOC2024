grid = []
grid_used = []

def fill_from(i, j):
    grid_used[i][j] = True
    plant = grid[i][j]
    area = 1
    circumference = []
    for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
        if (not 0 <= i+dir[0] < len(grid)) or (not 0 <= j+dir[1] < len(grid[0])) or grid[i+dir[0]][j+dir[1]] != plant:
            circumference.append([dir[0] == 0,max(i, i+dir[0]), max(j, j+dir[1])])
            continue
        if grid_used[i+dir[0]][j+dir[1]]:
            continue
        a, c = fill_from(i+dir[0], j+dir[1])
        area += a
        circumference.extend(c)

    return area, circumference


def task1():
    global grid_used
    input_file = open("input.txt")
    for line in input_file.readlines():
        grid.append(list(line.strip()))

    grid_used = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid_used[i][j]:
                continue
            area, circumference = fill_from(i, j)
            total += area * len(circumference)
    return total


def task2():
    global grid_used
    grid_used = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid_used[i][j]:
                continue
            area, circumference = fill_from(i, j)
            n_fences = 0

            # Vertical
            fences = [f for f in circumference if f[0]]
            for i_f in range(len(grid)+1):
                fences_line = [f[1] for f in fences if f[2] == i_f]
                if len(fences_line) == 0:
                    continue
                fences_line.sort()
                n_fences += 1
                for n in range(len(fences_line)-1):
                    if fences_line[n]+1 != fences_line[n+1]:
                        n_fences += 1
                    elif (0 <= i_f < len(grid)) and grid[fences_line[n]][i_f] != grid[fences_line[n+1]][i_f] and grid[fences_line[n]][i_f-1] != grid[fences_line[n+1]][i_f-1]:
                        n_fences += 1

            total += area*n_fences*2

    return total

if __name__ == '__main__':
    print(task1())
    print(task2())