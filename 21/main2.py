import itertools
from functools import lru_cache

from tqdm import tqdm

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
numpad = {'A': (0,0), '0': (0,-1), '1': (-1,-2), '2': (-1,-1), '3': (-1,0),
          '4': (-2,-2), '5': (-2,-1), '6': (-2,0), '7': (-3,-2), '8': (-3,-1), '9': (-3,0)}
numpad_reverse = {v: k for k, v in numpad.items()}
dir_pad = {'A': (0,0), '^': (0,-1), '<': (1,-2), 'v': (1,-1), '>': (1,0)}
dir_pad_reverse = {v: k for k, v in dir_pad.items()}

def add_pos(pos1, pos2):
    return pos1[0] + pos2[0], pos1[1] + pos2[1]

def dist_pos(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

@lru_cache(maxsize=None)
def get_numpad_step(start, end, n_dir_pads):
    if start == end:
        return 1 # A

    start_pos = numpad[start]
    end_pos = numpad[end]
    dist = dist_pos(start_pos, end_pos)
    options = []
    for direction in directions:
        new_pos = add_pos(start_pos, directions[direction])
        if new_pos not in numpad_reverse:
            continue
        if dist_pos(new_pos, end_pos) < dist:
            options.append(1 + get_numpad_step(numpad_reverse[new_pos], end, n_dir_pads))
    return min(options)

@lru_cache(maxsize=None)
def get_dir_pad_step(start, end, n_dir_pads):
    if start == end:
        return ["A"]

    start_pos = dir_pad[start]
    end_pos = dir_pad[end]
    dist = dist_pos(start_pos, end_pos)
    options = []
    for direction in directions:
        new_pos = add_pos(start_pos, directions[direction])
        if new_pos not in dir_pad_reverse:
            continue
        if dist_pos(new_pos, end_pos) < dist:
            options.extend([direction + o for o in get_dir_pad_step(dir_pad_reverse[new_pos], end, n_dir_pads)])
    return options

def get_numpad_sequences(input, n_dir_pads):
    len_sequences = get_numpad_step("A", input[0])
    for i in range(len(input) - 1):
        len_sequences += get_numpad_step(input[i], input[i + 1])
    return len_sequences

num_dir_pads = 1

def task1():
    input_file = open("test.txt")
    inputs = [n.strip() for n in input_file.readlines()]
    total = 0
    for input in inputs:
        len_sequence = get_numpad_sequences(input, num_dir_pads)
        return len_sequence
        total += len_sequence * int(input.strip('A'))
    return total

def task2():
    pass

if __name__ == '__main__':
    print(task1())
    print(task2())