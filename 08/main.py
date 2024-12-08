import itertools

import numpy as np

antennas = {}

def task1():
    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        for j, c in enumerate(line.strip()):
            if c == '.':
                continue
            if c not in antennas:
                antennas[c] = []
            antennas[c].append([i,j])

    grid = np.zeros([50,50])
    for c in antennas:
        for a1, a2 in itertools.combinations(antennas[c], 2):
            p1 = [a1[0]*2-a2[0], a1[1]*2-a2[1]]
            p2 = [a2[0]*2-a1[0], a2[1]*2-a1[1]]
            if 0 <= p1[0] < 50 and 0 <= p1[1] < 50:
                grid[p1[0],p1[1]] = 1
            if 0 <= p2[0] < 50 and 0 <= p2[1] < 50:
                grid[p2[0],p2[1]] = 1
    return int(sum(sum(grid)))

def task2():
    grid = np.zeros([50, 50])
    for c in antennas:
        for a1, a2 in itertools.combinations(antennas[c], 2):
            diff = [a1[0]-a2[0], a1[1]-a2[1]]
            for x in range(-50,50):
                p = [a1[0]+diff[0]*x, a1[1]+diff[1]*x]
                if 0 <= p[0] < 50 and 0 <= p[1] < 50:
                    grid[p[0],p[1]] = 1

    return int(sum(sum(grid)))

if __name__ == '__main__':
    print(task1())
    print(task2())