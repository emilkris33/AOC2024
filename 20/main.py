from itertools import count

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
grid = []

def task1():
    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        grid.append([n for n in line.strip()])
        if 'S' in line:
            start = [i, line.find('S')]
        if 'E' in line:
            end = [i, line.find('E')]

    to_process = [end]
    grid[end[0]][end[1]] = 0

    while len(to_process) > 0:
        current = to_process.pop(0)

        for direction in directions:
            next = [current[0] + direction[0], current[1] + direction[1]]
            temp_score = grid[current[0]][current[1]] + 1

            if (not 0 <= next[0] < len(grid)) or (not 0 <= next[1] < len(grid[0])) or grid[next[0]][next[1]] == '#':
                continue

            next_val = grid[next[0]][next[1]]
            if type(next_val) is not int or next_val > temp_score:
                grid[next[0]][next[1]] = temp_score
                if next not in to_process:
                    to_process.append(next)

    dist = 2
    num_cheats = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if type(val) is not int:
                continue
            for ii in range(i-dist, i+1+dist):
                for jj in range(j-dist, j+1+dist):
                    if (not 0 <= ii < len(grid)) or (not 0 <= jj < len(grid[0])):
                        continue
                    if abs(ii-i)+abs(jj-j)!=dist:
                        continue
                    if type(grid[ii][jj]) is not int:
                        continue
                    cheat_n = grid[i][j] - grid[ii][jj]-dist
                    if cheat_n >= 100:
                        num_cheats += 1
    return num_cheats



def task2():
    dist = 20
    num_cheats = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if type(val) is not int:
                continue
            for ii in range(i - dist, i + 1 + dist):
                for jj in range(j - dist, j + 1 + dist):
                    if (not 0 <= ii < len(grid)) or (not 0 <= jj < len(grid[0])):
                        continue
                    cheat_dist = abs(ii - i) + abs(jj - j)
                    if cheat_dist > dist:
                        continue
                    if type(grid[ii][jj]) is not int:
                        continue
                    cheat_n = grid[i][j] - grid[ii][jj] - cheat_dist
                    if cheat_n >= 100:
                        num_cheats += 1
    return num_cheats

if __name__ == '__main__':
    print(task1())
    print(task2())