from copy import deepcopy

grid_original = []
start_pos = []
instructions = []
grid = []

directions = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}


def push_box(position, direction):
    target = [position[0] + direction[0], position[1] + direction[1]]
    if grid[target[0]][target[1]] == '.':
        grid[target[0]][target[1]] = 'O'
        return True
    elif grid[target[0]][target[1]] == 'O':
        return push_box(target, direction)
    return False


def task1():
    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        if len(line.strip()) == 0:
            continue
        elif line[0] == '#':
            grid_original.append(list(line.strip()))
            if '@' in line:
                global start_pos
                start_pos = [i, line.find('@')]
        else:
            instructions.extend(list(line.strip()))

    global grid
    grid = deepcopy(grid_original)
    pos = start_pos

    for instruction in instructions:
        direction = directions[instruction]
        target = [pos[0]+direction[0], pos[1]+direction[1]]
        if grid[target[0]][target[1]] == '.':
            grid[target[0]][target[1]] = '@'
            grid[pos[0]][pos[1]] = '.'
            pos = target
        elif grid[target[0]][target[1]] == 'O':
            if push_box(target, direction):
                grid[target[0]][target[1]] = '@'
                grid[pos[0]][pos[1]] = '.'
                pos = target

    total = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == 'O':
                total += 100*i + j
    return total


grid_big = []


def push_vertical(position, direction, check_only):
    target = [position[0] + direction[0], position[1] + direction[1]]
    if grid_big[target[0]][target[1]] == '.':
        if not check_only:
            grid_big[target[0]][target[1]] = grid_big[position[0]][position[1]]
            grid_big[position[0]][position[1]] = '.'
        return True
    elif grid_big[target[0]][target[1]] == '[':
        if push_vertical(target, direction, check_only) and push_vertical([target[0], target[1]+1], direction, check_only):
            if not check_only:
                grid_big[target[0]][target[1]] = grid_big[position[0]][position[1]]
                grid_big[position[0]][position[1]] = '.'
            return True
    elif grid_big[target[0]][target[1]] == ']':
        if push_vertical(target, direction, check_only) and push_vertical([target[0], target[1]-1], direction, check_only):
            if not check_only:
                grid_big[target[0]][target[1]] = grid_big[position[0]][position[1]]
                grid_big[position[0]][position[1]] = '.'
            return True

    return False


def push_big_box(position, direction):
    # Horizontal push Easy
    if direction[0] == 0:
        target = [position[0] + direction[0], position[1] + direction[1]]
        if grid_big[target[0]][target[1]] == '.':
            grid_big[target[0]][target[1]] = grid_big[position[0]][position[1]]
            return True
        elif grid_big[target[0]][target[1]] in ['[', ']']:
            if push_big_box(target, direction):
                grid_big[target[0]][target[1]] = grid_big[position[0]][position[1]]
                return True
        return False


    # Vertical push Hard
    if grid_big[position[0]][position[1]] == '[':
        if push_vertical(position, direction, True) and push_vertical([position[0],position[1] + 1], direction, True):
            push_vertical(position, direction, False)
            push_vertical([position[0],position[1] + 1], direction, False)
            return True
    elif grid_big[position[0]][position[1]] == ']':
        if push_vertical(position, direction, True) and push_vertical([position[0],position[1] - 1], direction, True):
            push_vertical(position, direction, False)
            push_vertical([position[0],position[1] - 1], direction, False)
            return True

    return False


def task2():
    for line in grid_original:
        grid_big.append([])
        for char in line:
            if char == '#':
                grid_big[-1].extend(['#', '#'])
            elif char == 'O':
                grid_big[-1].extend(['[', ']'])
            elif char == '.':
                grid_big[-1].extend(['.', '.'])
            elif char == '@':
                grid_big[-1].extend(['@', '.'])

    pos = [start_pos[0], start_pos[1] * 2]
    
    for instruction in instructions:
        direction = directions[instruction]
        target = [pos[0]+direction[0], pos[1]+direction[1]]
        if grid_big[target[0]][target[1]] == '.':
            grid_big[target[0]][target[1]] = '@'
            grid_big[pos[0]][pos[1]] = '.'
            pos = target
        elif grid_big[target[0]][target[1]] in ['[', ']']:
            if push_big_box(target, direction):
                grid_big[target[0]][target[1]] = '@'
                grid_big[pos[0]][pos[1]] = '.'
                pos = target

    total = 0
    for i, line in enumerate(grid_big):
        for j, char in enumerate(line):
            if char == '[':
                total += 100 * i + j
    return total

if __name__ == '__main__':
    print(task1())
    print(task2())