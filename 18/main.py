import re
from unittest.mock import patch

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def compare_pos(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

def pos_string(pos):
    return f"{pos[0]},{pos[1]}"

def reconstruct_path(came_from, current):
    path = [current]
    while pos_string(current) in came_from:
        current = came_from[pos_string(current)]
        path.append(current)
    path.reverse()
    return path

def min_path(grid):
    start = [0, 0]
    end = [70, 70]

    to_search = [start]
    came_from = {}

    g_score = {pos_string(start): 0}
    f_score = {pos_string(start): 140}

    while len(to_search) > 0:
        to_search.sort(key=lambda pos: f_score[pos_string(pos)], reverse=True)
        current = to_search.pop()
        current_str = pos_string(current)
        if compare_pos(current, end):
            return reconstruct_path(came_from, current)

        for direction in directions:
            next = [current[0] + direction[0], current[1] + direction[1]]
            temp_g_score = g_score[current_str] + 1

            if (not 0 <= next[0] <= 70) or (not 0 <= next[1] <= 70) or grid[next[0]][next[1]] > 0:
                continue

            next_str = pos_string(next)
            if next_str not in g_score or temp_g_score < g_score[next_str]:
                came_from[next_str] = current
                g_score[next_str] = temp_g_score
                f_score[next_str] = temp_g_score + 140 - next[0] - next[1]
                if next not in to_search:
                    to_search.append(next)

    return None


def task1():
    grid = [[0 for _ in range(71)] for _ in range(71)]

    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        if i >= 1024:
            break
        p = [int(n) for n in re.findall(r"\d+", line)]
        grid[p[0]][p[1]] = 1

    path = min_path(grid)

    return len(path) - 1

def task2():
    grid = [[0 for _ in range(71)] for _ in range(71)]

    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        p = [int(n) for n in re.findall(r"\d+", line)]
        grid[p[0]][p[1]] = 1

        if i < 2900:
            continue

        if min_path(grid) is None:
            return line


if __name__ == '__main__':
    print(task1())
    print(task2())