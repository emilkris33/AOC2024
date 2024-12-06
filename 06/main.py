
grid = []
start_i = 0
start_j = 0

def task1():
    global start_i
    global start_j
    input_file = open("input.txt")
    for n, line in enumerate(input_file.readlines()):
        grid.append(list(line.strip()))
        if '^' in line:
            start_i = n
            start_j = line.index('^')

    i = start_i
    j = start_j
    direction = [-1, 0]
    while 0 <= i < 130 and 0 <= j < 130:
        grid[i][j] = 'X'
        while grid[i+direction[0]][j+direction[1]] == '#':
            direction = [direction[1], -direction[0]]
        i = i+direction[0]
        j = j+direction[1]

    return sum(x.count('X') for x in grid)

def task2():
    count = 0

    for obstacle_i in range(130):
        for obstacle_j in range(130):
            i = start_i
            j = start_j
            direction = [-1, 0]
            if grid[obstacle_i][obstacle_j] != 'X':
                continue
            for n in range(10000):
                if not (0 <= i < 130 and 0 <= j < 130):
                    break
                while (0 <= i + direction[0] < 130) and (0 <= j + direction[1] < 130) and ((grid[i + direction[0]][j + direction[1]] == '#') or (i + direction[0] == obstacle_i and j + direction[1] == obstacle_j)):
                    direction = [direction[1], -direction[0]]
                i = i + direction[0]
                j = j + direction[1]
            else:
                count += 1
    return count

if __name__ == '__main__':
    print(task1())
    print(task2())