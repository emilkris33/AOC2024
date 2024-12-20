from functools import lru_cache

@lru_cache(maxsize=None)
def is_possible(pattern):
    options = 0
    for towel in towels:
        if pattern.startswith(towel):
            if len(pattern) == len(towel):
                options += 1
            else:
                options += is_possible(pattern[len(towel):])
    return options


def task1():
    global towels
    global patterns
    input_file = open("input.txt")
    towels = [t.strip() for t in input_file.readline().split(',')]

    input_file.readline()
    patterns = [p.strip() for p in input_file.readlines()]

    num_possible = 0
    for pattern in patterns:
        if is_possible(pattern):
            num_possible += 1

    return num_possible


def task2():
    num_options = 0
    for pattern in patterns:
        num_options += is_possible(pattern)

    return num_options

if __name__ == '__main__':
    print(task1())
    print(task2())