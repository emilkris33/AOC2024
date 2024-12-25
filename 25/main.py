from numpy.ma.core import outer

reading = []
keys = []
locks = []

def do_read():
    global reading
    nums = [-1 for _ in range(5)]
    for read in reading:
        for i, char in enumerate(read):
            if char == '#':
                nums[i] += 1
    if reading[0] == "#####":
        keys.append(nums)
    else:
        locks.append(nums)
    reading = []

def task1():
    input_file = open("input.txt")
    for line in input_file.readlines():
        line = line.strip()
        if len(line) > 0:
            reading.append(line)
        else:
            do_read()
    do_read()

    output = 0
    for key in keys:
        for lock in locks:
            for i in range(5):
                if key[i] + lock[i] > 5:
                    break
            else:
                output += 1
    return output



def task2():
    pass

if __name__ == '__main__':
    print(task1())
    print(task2())