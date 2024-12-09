from copy import deepcopy

from tqdm import tqdm

file_system = []

def task1():
    input_file = open("input.txt")
    file_num = 0
    for idx, char in enumerate(input_file.readline().strip()):
        if idx % 2 == 0:
            file_system.extend([file_num for _ in range(int(char))])
            file_num += 1
        else:
            file_system.extend([None for _ in range(int(char))])

    file_system_1 = deepcopy(file_system)
    idx = len(file_system_1)
    insert_idx = 0
    while idx > 0:
        idx -= 1
        if file_system_1[idx] is None:
            continue
        while file_system_1[insert_idx] is not None:
            insert_idx += 1
        if insert_idx >= idx:
            break
        file_system_1[insert_idx] = file_system_1[idx]
        file_system_1[idx] = None
    total = 0
    for i, x in enumerate(file_system_1):
        if x is None:
            break
        total += i * x
    return total


def task2():
    start_index_idx = 0
    for file_to_move in tqdm(range(file_system[-1], 0, -1)):
        to_move_idx = next(i for i, x in enumerate(file_system) if x == file_to_move)
        to_move_length = next((i for i, x in enumerate(file_system[to_move_idx:]) if x != file_to_move), len(file_system)-to_move_idx)
        pass

        insert_idx = start_index_idx
        while not all(n is None for n in file_system[insert_idx:insert_idx+to_move_length]):
            if insert_idx >= to_move_idx:
                break
            insert_idx += 1
        if insert_idx >= to_move_idx:
            continue
        if to_move_length == 1:
            start_index_idx = insert_idx + 1
        file_system[insert_idx:insert_idx+to_move_length] = file_system[to_move_idx:to_move_idx+to_move_length]
        file_system[to_move_idx:to_move_idx+to_move_length] = [None for _ in range(to_move_length)]
    total = 0
    for i, x in enumerate(file_system):
        if x is None:
            continue
        total += i * x
    return total

if __name__ == '__main__':
    print(task1())
    print(task2())