import re
from math import floor, ceil

robots = []

width = 101
width_middle = ceil(width / 2) - 1
height = 103
height_middle = ceil(height / 2) - 1

def task1():
    input_file = open("input.txt")
    for line in input_file.readlines():
        robot = [int(n) for n in re.search(r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()]
        robots.append(robot)

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        p_100 = [(robot[0] + robot[2]*100)%width, (robot[1] + robot[3]*100)%height]
        if p_100[0] < width_middle:
            if p_100[1] < height_middle:
                q1 += 1
            elif p_100[1] > height_middle:
                q2 += 1
        elif p_100[0] > width_middle:
            if p_100[1] < height_middle:
                q3 += 1
            elif p_100[1] > height_middle:
                q4 += 1

    return  q1 * q2 * q3 * q4

def check_grid(grid):
    for line in grid:
        for char in line:
            if char == 2:
                return False
    return True


def task2():
    for n in range(10000):
        grid = [[0 for _ in range(width)] for _ in range(height)]
        for robot in robots:
            p_n = [(robot[0] + robot[2] * n) % width, (robot[1] + robot[3] * n) % height]
            grid[p_n[1]][p_n[0]] += 1
        if check_grid(grid):
            print(f"Iteration {n}")
            for line in grid:
                for char in line:
                    if char == 0:
                        print(' ', end='')
                    else:
                        print(char, end='')
                print()


if __name__ == '__main__':
    print(task1())
    print(task2())